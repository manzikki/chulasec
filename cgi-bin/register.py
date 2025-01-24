#!/usr/bin/env python3

import cgi
import cgitb
import os

# Enable debugging (disable in production)
cgitb.enable()

# File to store the credentials
PASSWORDS_FILE = "passwords.txt"

# Print HTTP headers
print("Content-Type: text/html\n")

# Retrieve form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
confirm_password = form.getvalue("confirmPassword")

# Ensure all fields are filled
if not username or not password or not confirm_password:
    print("<html><body><h1>Error: All fields are required.</h1>")
    print('<a href="/register.html">Go Back</a></body></html>')
else:
    # Check if passwords match
    if password == confirm_password:
        try:
            # Open the file in append mode
            with open(PASSWORDS_FILE, "a") as file:
                # Append the username and password (separated by a comma)
                file.write(f"{username},{password}\n")
            
            # Success message
            print("<html><body>")
            print(f"<h1>Welcome, {username}! Registration successful.</h1>")
            print('<a href="/">Go to Login</a>')
            print("</body></html>")
        except Exception as e:
            # Handle any errors during file writing
            print("<html><body><h1>Error: Could not save your information.</h1>")
            print(f"<p>{e}</p>")
            print('<a href="/register.html">Go Back</a></body></html>')
    else:
        # Passwords don't match
        print("<html><body><h1>Error: Passwords do not match.</h1>")
        print('<a href="/register.html">Go Back</a></body></html>')
