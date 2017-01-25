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
import validators

# html boilerplate for the top of every page
page_header = """
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

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        add_form = """
        <form action="/add" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input type="text" name="user-name"/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input type="password" name="password1"/>
                        <td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input type="password" name="password2"/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input type="email" name="email"/>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" value="Submit"/>
        </form>
        """



# make form for signup fields
#make submit button
#make successful redirect page
#validate inputs



        content = page_header + add_form +  page_footer
        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
