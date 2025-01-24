#!/usr/bin/env python3

import cgi
import html

# Set the Content-Type header for the response
print("Content-Type: text/html\n")

# Get the form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Read the usenames and passwords from the file
# File to store the credentials
PASSWORDS_FILE = "passwords.txt"
credentials = {}

# Read the file and populate the dictionary
try:
    with open(PASSWORDS_FILE, "r") as file:
        for line in file:
            # Strip whitespace and split by the comma
            u, p = line.strip().split(",")
            # Add to the dictionary
            credentials[u] = p
except FileNotFoundError:
    print(f"Error: {PASSWORDS_FILE} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Check the credentials

if username in credentials and credentials[username] == password:
    # If login is successful, redirect to main.html
    print('<html><body>')
    print('<h1>Login successful!</h1>')
    print('<meta http-equiv="refresh" content="2;url=/main.html">')  # Redirect after 2 seconds
    print('</body></html>')
else:
    # If login fails, show an error and a "Go back" button
    print('<html><body>')
    print('<h1>Invalid credentials, please try again.</h1>')
    print('<form action="../index.html">')  # Form to go back to the login page
    print('<button type="submit">Go Back</button>')
    print('</form>')
    print('</body></html>')
