original = """Delivered-To: tanishq.aggarwal.11@gmail.com
Received: by 10.103.116.193 with SMTP id p184csp2151301vsc;
        Tue, 25 Jul 2017 11:56:07 -0700 (PDT)
X-Received: by 10.55.20.144 with SMTP id 16mr24913439qku.51.1501008967318;
        Tue, 25 Jul 2017 11:56:07 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1501008967; cv=none;
        d=google.com; s=arc-20160816;
        b=xmai5voPTV/RjGYi7CmpVbJteGJ7RcBBHG5JKL7I7gfKrJ3aEQ6pQ9A1TxC/m/2pHz
         43fH4MV6Z78cx+bHkXZ1eQxka5DygaDaiJ/t5+LhglsPItufJSU6bVgmHwz0yUCmAGxk
         KJB774u96FdZLBfClVO2ZJ7U1U0B49VrJaol9/ml5eZqIW3CXSq8FTKg3VZVsI8RabRP
         UXEwSwqoqVrBVODLRorl5moXnjuaT6mCabY3vNwH0/NzyEgVnHmPuxetO3ofzHp7Ds8j
         vJAcbmpXaexjqS5weM8yBfOs0gC/wQK8RlLVBkfc07tjSxAw3IsfxogwL7SGCTGWoI5a
         UfhA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:references:in-reply-to:mime-version
         :arc-authentication-results;
        bh=mSkQCAdQsRxTUHY+IsyDlp8xqjCAtKy73oM2Ue/6Ww8=;
        b=TLRKAljZ+9LNhA7uygv/EYYgW7LdNTx8yYZij5Imny5NoKtfVLSCele4nScfDNEVMX
         9yNd8HNOxOOd378Mdzx93JDcjbcfwmetzKDu5c5OQHhfk80F/00rmU9KK43IhnrR9nRC
         DZhh8xhQrHyZqUjsI9PJ5COgpsY++Qeo+y9mtesS8AR3o80FSjwSGE6sFux1sofZsaec
         VqFjuDKuuVz46mjsNDuuFmvMRgXmox7aQh070X1GC2cmOF8v0tXQqosEVzVOHoA0C0yb
         LhGwfHi6aEUPkmVjlHWzdHxJyxGUUYsuAu9RnjI3CnwdWgTl4aUCoweoBdDgess5m5Pn
         sCGw==
ARC-Authentication-Results: i=1; mx.google.com;
       spf=pass (google.com: domain of ta335@cornell.edu designates 128.84.13.242 as permitted sender) smtp.mailfrom=ta335@cornell.edu
Return-Path: <ta335@cornell.edu>
Received: from limerock02.mail.cornell.edu (limerock02.mail.cornell.edu. [128.84.13.242])
        by mx.google.com with ESMTP id 30si11557428qtf.266.2017.07.25.11.56.07
        for <tanishq.aggarwal.11@gmail.com>;
        Tue, 25 Jul 2017 11:56:07 -0700 (PDT)
Received-SPF: pass (google.com: domain of ta335@cornell.edu designates 128.84.13.242 as permitted sender) client-ip=128.84.13.242;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of ta335@cornell.edu designates 128.84.13.242 as permitted sender) smtp.mailfrom=ta335@cornell.edu
X-CornellRouted: This message has been Routed already.
Received: from exchange.cornell.edu (sf-e2013-06.exchange.cornell.edu [10.22.40.53]) by limerock02.mail.cornell.edu (8.14.4/8.14.4_cu) with ESMTP id v6PItvgZ013013 for <tanishq.aggarwal.11@gmail.com>; Tue, 25 Jul 2017 14:56:06 -0400
Received: from sf-e2013-03.exchange.cornell.edu (10.22.40.50) by sf-e2013-06.exchange.cornell.edu (10.22.40.53) with Microsoft SMTP Server (TLS) id 15.0.1210.3; Tue, 25 Jul 2017 14:56:05 -0400
Received: from mail-lf0-f70.google.com (209.85.215.70) by exchange.cornell.edu (10.22.40.50) with Microsoft SMTP Server (TLS) id 15.0.1210.3 via Frontend Transport; Tue, 25 Jul 2017 14:56:05 -0400
Received: by mail-lf0-f70.google.com with SMTP id f26so34441145lfh.14
        for <tanishq.aggarwal.11@gmail.com>; Tue, 25 Jul 2017 11:56:05 -0700 (PDT)
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20161025;
        h=x-gm-message-state:mime-version:in-reply-to:references:from:date
         :message-id:subject:to;
        bh=mSkQCAdQsRxTUHY+IsyDlp8xqjCAtKy73oM2Ue/6Ww8=;
        b=QosogqOhFuPDDIzY4YG3I3Z3/XNV45sxq82t6ot3lwbWPCPkCn8ZXpJbp1PWdNiIVe
         d+3VfwM6MJUntMHcvt/8rjbez+2HSCpDEI0iJktAh3K/+iuATHLvxrXuQzKsqOEBEupl
         2GfRr0QlEYf79tY269Sp7TSsfj/rloQjkuOun4LY28O3iBrQXO4sI39q7ubjiq1JQ/kp
         y3hW32XQ95BGm1/GdyvbcXY3uKyEkYfwfjno/rNaCtzcYrPQWGnlIZYmFXHVP25rzrZ8
         gUvDp86tqTHQPivhew9IXu9RQDTXDi14momPYe0ZTfY3g5pexeMDDcbgBRMOngR100oQ
         ip7w==
X-Gm-Message-State: AIVw1102h0HHdbVfxUHc+aQdwP0U1B7FfUkp4hXqv2FKTZ21XjM1n0E4 D5QRv0t+cbA35JGaV8Ll0Nl/ee7qmqymSrptBAfEkFZMK6cgbRYTq6069h/A65XggFTZ0BGJWBi XATUJTo0jfIO9ZMck7q7qw7LZYA50nPoq6GmYqW5uiQiG
X-Received: by 10.25.145.10 with SMTP id t10mr2985944lfd.23.1501008963761;
        Tue, 25 Jul 2017 11:56:03 -0700 (PDT)
X-Received: by 10.25.145.10 with SMTP id t10mr2985942lfd.23.1501008963613; Tue, 25 Jul 2017 11:56:03 -0700 (PDT)
MIME-Version: 1.0
Received: by 10.25.26.137 with HTTP; Tue, 25 Jul 2017 11:56:02 -0700 (PDT)
In-Reply-To: <201707241732.v6OHWgfj009678@sws2.sas.cornell.edu>
References: <201707241732.v6OHWgfj009678@sws2.sas.cornell.edu>
From: Tanishq Aggarwal <ta335@cornell.edu>
Date: Tue, 25 Jul 2017 14:56:02 -0400
Message-ID: <CAH9NSGb6xBiQRLoZtNieL+=W7R8y0oUwyPv+RcsN3_Q8cAR87Q@mail.gmail.com>
Subject: Fwd: Congratulations and Welcome From your Cornell Orientation Leader!
To: <tanishq.aggarwal.11@gmail.com>
Content-Type: multipart/alternative; boundary="94eb2c1cd49c14ce49055528e2ed"
Received-SPF: Pass (sf-e2013-06.exchange.cornell.edu: domain of ta335@cornell.edu designates 209.85.215.70 as permitted sender) receiver=sf-e2013-06.exchange.cornell.edu; client-ip=209.85.215.70; helo=mail-lf0-f70.google.com;
X-ORG-HybridRouting: 893f188ca8e1f3b8d549a9577746145b
X-ORG-RouteOnPrem: False
X-ORG-MsgSource: cmail
X-PMX-CORNELL-AUTH-RESULTS: dkim-out=none;

--94eb2c1cd49c14ce49055528e2ed
Content-Type: text/plain; charset="UTF-8"

---------- Forwarded message ----------
From: Sam Ognisty <sjo44@cornell.edu>
Date: Mon, Jul 24, 2017 at 1:32 PM
Subject: Congratulations and Welcome From your Cornell Orientation Leader!
To: Tanishq Aggarwal <ta335@cornell.edu>


Hi Tanishq,

First off, let me introduce myself. My name is Sam Ognisty and I will be
your Orientation Leader for the Fall 2017 semester! I can't wait to meet
you and I'm sure you are also looking forward to attending Cornell this
fall. I personally don't know what expectations or possible fears you have
for your first semester at Cornell, but let me assure you now that you will
definitely enjoy your Orientation at Cornell! You will meet a lot of fun
and interesting people from all over the world, and you may even meet some
of the people that will become your best friends. We have a lot of events
planned in order to introduce you to the campus and your fellow incoming
Freshman.

If you have any academic questions, I am a junior studying Mechanical
Engineering, planning on minoring in Aerospace Engineering. But feel free
to ask any questions you may have. I'll do my best to answer them!

I can't wait to meet you this fall, and I hope that you enjoy the rest of
your summer. Feel free to contact me via email (sjo44@cornell.edu) before
move-in day if you have any questions.

Sam Ognisty

--94eb2c1cd49c14ce49055528e2ed
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><br><div class=3D"gmail_quote">---------- Forwarded messag=
e ----------<br>From: <b class=3D"gmail_sendername">Sam Ognisty</b> <span d=
ir=3D"ltr">&lt;<a href=3D"mailto:sjo44@cornell.edu">sjo44@cornell.edu</a>&g=
t;</span><br>Date: Mon, Jul 24, 2017 at 1:32 PM<br>Subject: Congratulations=
 and Welcome From your Cornell Orientation Leader!<br>To: Tanishq Aggarwal =
&lt;<a href=3D"mailto:ta335@cornell.edu">ta335@cornell.edu</a>&gt;<br><br><=
br>Hi Tanishq,<br>
<br>
First off, let me introduce myself. My name is Sam Ognisty and I will be yo=
ur Orientation Leader for the Fall 2017 semester! I can&#39;t wait to meet =
you and I&#39;m sure you are also looking forward to attending Cornell this=
 fall. I personally don&#39;t know what expectations or possible fears you =
have for your first semester at Cornell, but let me assure you now that you=
 will definitely enjoy your Orientation at Cornell! You will meet a lot of =
fun and interesting people from all over the world, and you may even meet s=
ome of the people that will become your best friends. We have a lot of even=
ts planned in order to introduce you to the campus and your fellow incoming=
 Freshman.<br>
<br>
If you have any academic questions, I am a junior studying Mechanical Engin=
eering, planning on minoring in Aerospace Engineering. But feel free to ask=
 any questions you may have. I&#39;ll do my best to answer them!<br>
<br>
I can&#39;t wait to meet you this fall, and I hope that you enjoy the rest =
of your summer. Feel free to contact me via email (<a href=3D"mailto:sjo44@=
cornell.edu">sjo44@cornell.edu</a>) before move-in day if you have any ques=
tions.<br>
<span class=3D"HOEnZb"><font color=3D"#888888"><br>
Sam Ognisty<br>
</font></span></div><br></div>

--94eb2c1cd49c14ce49055528e2ed--"""
import re

message = original.splitlines()
froms = []
for line in message:
    if line[0:5] == "From:":
        froms.append(line)

people = []
for person in froms:
    splitperson = person.split()[1:]
    print(splitperson)
    email_address = re.search(r'[\w\.-]+@cornell.edu+', splitperson[2]).group(0)
    if email_address == "":
        continue


    # newperson = Cornellian()
    # newperson.first_name = splitperson[0]
    # newperson.last_name = splitperson[1]
    # newperson.email_address = email_address

    people.append({
    	"first_name" : splitperson[0],
    	"last_name" : splitperson[1],
    	"email_address" : email_address,
    })

print(people)