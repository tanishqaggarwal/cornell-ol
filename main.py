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
import re
from google.appengine.ext import ndb
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), 
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

##DATABASE
class Cornellian(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_name  = ndb.StringProperty(required = True)
    email_address = ndb.StringProperty(required = True)

class Orientation(ndb.Model):
    leader = ndb.StructuredProperty(Cornellian, required = True)
    followers = ndb.StructuredProperty(Cornellian, repeated = True)

##HANDLERS
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(JINJA_ENVIRONMENT.get_template("index.html").render())

class ViewOrientation(webapp2.RequestHandler):
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
                members = orientation.followers
                orientation_members = []
                if members:
                    cornellians = Cornellian.query(Cornellian.email_address.IN(members)).fetch()
                    for cornellian in cornellians:
                        class_members.append({
                            "first_name"    : cornellian.first_name,
                            "last_name"     : cornellian.last_name,
                            "email_address" : cornellian.email_address,
                        })
                self.response.out.write(JINJA_ENVIRONMENT.get_template("view_orientation.html").render({"orientation_members" : orientation_members}))
        except Exception as e:
            logging.error(e)
            self.response.out.write(JINJA_ENVIRONMENT.get_template("view_orientation_error.html").render())

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        message = str(mail_message.original).splitlines()
        froms = []
        for line in message:
            if line[0:5] == "From:":
                froms.append(line)

        people = []
        for person in froms:
            splitperson = person.split()
            email_address = re.search(r'[\w\.-]+@cornell.edu+', splitperson[2]).group(0)
            if email_address == "":
                continue

            newperson = Cornellian()
            newperson.first_name = splitperson[0]
            newperson.last_name = splitperson[1]
            newperson.email_address = email_address

            people.append(newperson)

        ndb.put_multi(people)

        orientation = Orientation.query(Orientation.leader.email_address == people[1].email_address).fetch()
        if orientation == [] or orientation == None:
            orientation = Orientation()
            orientation.leader = people[1]
            orientation.followers.append(people[0])
            orientation.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/view/orientation', ViewOrientation),
    LogSenderHandler.mapping(),
], debug=True)