#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()  # Enable for debugging (disable in production)

# Print HTTP headers
print("Content-Type: text/html\n")

# Retrieve form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
confirm_password = form.getvalue("confirmPassword")

# Process registration (example logic)
if password == confirm_password:
    print(f"<html><body><h1>Welcome, {username}! Registration successful.</h1></body></html>")
else:
    print("<html><body><h1>Error: Passwords do not match!</h1></body></html>")
