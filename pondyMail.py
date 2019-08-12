#!/usr/bin/env python


COMMAND = "ipconfig" 
EMAIL = "your-email@gmail.com"
PASSWORD = "password"

from subprocess import check_output
import smtplib

output = check_output(COMMAND, shell=True)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your-email, password)
message = " ** here is your report  ** \n"
message = message + "Result of " + COMMAND + "\n"
server.sendmail(EMAIL, EMAIL, message + output)
server.quit()