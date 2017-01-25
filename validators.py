#validators
import re

User_Re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
Pass_Re = re.compile(r"^.{3,20}$")
Email_Re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return User_Re.match(username)

def valid_password(password):
    return Pass_Re.match(password)

def valid_email(email):
    return Email_Re.match(email)

def verify_password(password1, password2)
    if password1 == password2:
        return True
    return False


email = "z@a.a"

print(valid_email(email))
