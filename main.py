#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import logging
import urllib
import os
import re
from google.appengine.ext import ndb
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), 
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

##DATABASE
class Cornellian(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_name  = ndb.StringProperty(required = True)
    email_address = ndb.StringProperty(required = True)
    subscribed    = ndb.BooleanProperty(default = True)

class Orientation(ndb.Model):
    leader = ndb.StructuredProperty(Cornellian, required = True)
    followers = ndb.StructuredProperty(Cornellian, repeated = True)

##HANDLERS
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(JINJA_ENVIRONMENT.get_template("index.html").render())

class ViewOrientation(webapp2.RequestHandler):
    #Gets followers in an orientation and the leader, and outputs the data to the template data.
    def get(self):
        try:
            leader_id = self.request.get("leader_id")
            orientation = Orientation.query(Orientation.leader.email_address == leader_id).get()
            if not orientation:
                raise Exception()
            else:
                leader_info = {
                    "first_name" : orientation.leader.first_name,
                    "last_name" : orientation.leader.last_name,
                    "email_address" : orientation.leader.email_address,
                }
                members = [follower.email_address for follower in orientation.followers]
                orientation_members = []
                if members:
                    cornellians = Cornellian.query(Cornellian.email_address.IN(members)).fetch()
                    for cornellian in cornellians:
                        orientation_members.append({
                            "first_name"    : cornellian.first_name,
                            "last_name"     : cornellian.last_name,
                            "email_address" : cornellian.email_address,
                        })
                self.response.out.write(JINJA_ENVIRONMENT.get_template("view_orientation.html").render({"leader_info" : leader_info, "orientation_members" : orientation_members}))
        except Exception as e:
            logging.error(e)
            self.response.out.write(JINJA_ENVIRONMENT.get_template("view_orientation_error.html").render())

class LogSenderHandler(InboundMailHandler):
    #Receives message sent to the server, takes any email addresses found within the content of the email, and creates 
    def receive(self, mail_message):
        message = mail_message.bodies('text/plain')
        for content_type, body in message:
            decoded_message = body.decode().splitlines()
            email_addresses = []
            for line in decoded_message:
                if line[0:5] == "From:" or line[0:3] == "To:":
                    email_addresses.append(line)

            new_people = []
            old_people = []
            for email in email_addresses:
                splitperson = email.split()[1:] #Removes the "From:" or "To:"
                email_address = splitperson[2][1:-1] #Converts "<email@cornell.edu>" to "email@cornell.edu"

                cornellian = Cornellian.query(Cornellian.email_address == email_address).get() 
                if not cornellian: #If cornellian is not in DB, then add them.
                    newperson = Cornellian()
                    newperson.first_name = splitperson[0]
                    newperson.last_name = splitperson[1]
                    newperson.email_address = email_address

                    new_people.append(newperson)
                else: #Otherwise, add them to the old people field. This has to be an OL, since by the nature of the application's design, all entities are added exactly once.
                    old_people.append(cornellian)

            ndb.put_multi(new_people)

            people = old_people + new_people
            leader   = people[0]
            follower = people[1]

            orientation = Orientation.query(Orientation.leader.email_address == leader.email_address).get()
            if not orientation:
                orientation = Orientation()
                orientation.leader = leader
                orientation.followers = []

            orientation.followers.append(follower)
            orientation.put()

            #Send email notification
            for cornellian in orientation.followers:
                if cornellian.subscribed == None:
                    cornellian.subscribed = True
                if cornellian.subscribed == True:
                    mail.send_mail(sender = "ta335@cornell.edu",
                    to=email,
                    subject="Notification: new classmate in Orientation group",
                    body="""Hi there,
{0} {1} ({2}) just joined your orientation group. Check the full list out <a href = "http://cornell-ol.appspot.com/view/orientation?leader_id={3}">here</a>!

If you would like to unsubscribe from these notifications, just let Tanishq know at ta335@cornell.edu.
                    """.format(follower.first_name, follower.last_name, follower.email_address, leader.email_address))
            
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/view/orientation', ViewOrientation),
    LogSenderHandler.mapping(),
], debug=True)