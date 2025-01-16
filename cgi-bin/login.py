#!/usr/bin/env python3

import cgi
import html

# Set the Content-Type header for the response
print("Content-Type: text/html\n")

# Get the form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Check the credentials
if username == "foo" and password == "bar":
    # If login is successful, redirect to main.html
    print('<html><body>')
    print('<h1>Login successful!</h1>')
    print('<meta http-equiv="refresh" content="2;url=/main.html">')  # Redirect after 2 seconds
    print('</body></html>')
else:
    # If login fails, show an error and a "Go back" button
    print('<html><body>')
    print('<h1>Invalid credentials, please try again.</h1>')
    print('<form action="index.html">')  # Form to go back to the login page
    print('<button type="submit">Go Back</button>')
    print('</form>')
    print('</body></html>')
