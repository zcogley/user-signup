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
import re
import validators

# html boilerplate for the top of main page
main_page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style>.error {color: red; }</style>
    <style type="text/css"></style>
</head>
<body>
    <h1>Signup</h1>
"""

welcome_page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
"""

# html boilerplate for the bottom of every page

page_footer = """
</body>
</html>
"""

username_error = ""
password1_error = ""
password2_error = ""
email_error = ""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        error1 = self.request.get("error1")
        if error1 == "True":
            username_error = "That's not a valid username."
        else:
            username_error = ""

        error2 = self.request.get("error2")
        if error2 == "True":
            password1_error = "That's not a valid password."
        else:
            password1_error = ""

        error3 = self.request.get("error3")
        if error3 == "True":
            password2_error = "Your passwords don't match."
        else:
            password2_error = ""

        error4 = self.request.get("error4")
        if error4 == "True":
            email_error = "That's not a valid email."
        else:
            email_error = ""

        welcome_form = """
        <form action="/welcome" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input type="text" name="user-name"/>
                            <span class="error">{a}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input type="password" name="password1"/>
                            <span class="error">{b}</span>
                        <td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input type="password" name="password2"/>
                            <span class="error">{c}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input type="email" name="email"/>
                            <span class="error">{d}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" value="Submit"/>
        </form>
        """.format(a=username_error, b=password1_error, c=password2_error, d=email_error)

        content = main_page_header + welcome_form + page_footer
        self.response.write(content)

# not doing anything right now
    def post(self):
        content = main_page_header + welcome_form + page_footer
        self.response.write(content)

class WelcomeHandler(webapp2.RequestHandler):
    def post(self):
        # look inside the request to figure out what the user typed
        username = self.request.get("user-name")
        password1 = self.request.get("password1")
        password2 = self.request.get("password2")
        email = self.request.get("email")

        redirect = False
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not validators.valid_username(username):
            redirect = True
            error1 = "True"

        if not validators.valid_password(password1):
            redirect = True
            error2 = "True"

        if password1 != password2:
            redirect = True
            error3 = "True"

        if not validators.valid_email(email) and email != "":
            redirect = True
            error4 = "True"

        if redirect == True:
            self.redirect('/?error1=' + error1 + '&error2=' + error2 + '&error3=' + error3 + '&error4=' + error4)

        sentence = "Welcome, " + username + "!"
        content = welcome_page_header + "<h1>" + sentence + "</h1>" + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)


#validate inputs
#make error variable
#need to look at user input and if ""
