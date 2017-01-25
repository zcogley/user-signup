questions:
(1) why aren't my validators importing correctly?
(2) how do I toggle the error messages on/off without the craziness I have?
(3) how do I get the validators to accept nothing as passing?



welcome_form_head = """
<form action="/welcome" method="post">
    <table>
        <tbody>"""

tableline1_orig = """
            <tr>
                <td>
                    <label for="username">Username</label>
                </td>
                <td>
                    <input type="text" name="user-name" value required/>
                </td>
            </tr>"""

tablelin1_err = """
            <tr>
                <td>
                    <label for="username">Username</label>
                </td>
                <td>
                    <input type=text" name="user-name" value required/>
                    <span class="error">That's not a valid username.</span>
                </td>
            </tr>"""

tableline2_orig ="""
            <tr>
                <td>
                    <label for="password">Password</label>
                </td>
                <td>
                    <input type="password" name="password1" value required/>
                <td>
            </tr>"""

tableline2_err ="""
            <tr>
                <td>
                    <label for="password">Password</label>
                </td>
                <td>
                    <input type="password" name="password1" value required/>
                    <span class="error">That's not a valid pasword.</span>
                <td>
            </tr>"""

tableline3_orig ="""
            <tr>
                <td>
                    <label for="verify">Verify Password</label>
                </td>
                <td>
                    <input type="password" name="password2" value required/>
                </td>
            </tr>"""

tableline3_err ="""
            <tr>
                <td>
                    <label for="verify">Verify Password</label>
                </td>
                <td>
                    <input type="password" name="password2" value required/>
                    <span class="error">Passwords don't match.</span>
                </td>
            </tr>"""

tableline4_orig ="""
            <tr>
                <td>
                    <label for="email">Email (optional)</label>
                </td>
                <td>
                    <input type="email" name="email" value required/>
                </td>
            </tr>"""

tableline4_err ="""
            <tr>
                <td>
                    <label for="email">Email (optional)</label>
                </td>
                <td>
                    <input type="email" name="email" value required/>
                    <span class="error">That's not a valid email.</span>
                </td>
            </tr>"""

welcome_form_foot = """
        </tbody>
    </table>
    <input type="submit" value="Submit"/>
</form>
"""
