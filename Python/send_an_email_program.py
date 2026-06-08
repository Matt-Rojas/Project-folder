import smtplib

sender = "rick.grimes@gmail.com"
receiver = "carl.grimes@gmail.com"
password = "Password1234"
subject = "THIS IS A TEST!!!"
body = "THIS IS A TEST, THIS IS CURRENTLY BEING WRITTEN THROUGH A PYTHON PROGRAM"

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")