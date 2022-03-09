import datetime
import os
import smtplib
import ssl
from time import sleep

port = 465 #ssl


host = input('What is the IP? ')
delay = input('How often do you want to check the host (seconds)? ')
emailTo =  input('In the event that the server goes down what email would you like to have notified? ')
password = input("Type your Password and press enter: ")

context = ssl.create_default_context()

  #does not send email yet but no error looking for fix
def downEmail():
  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(emailTo, password)

def send_ping_request():
    currentTime = datetime.datetime.now()
    response = os.system('ping ' + host)
    status = f'{currentTime} - {host}\n'
    file = open('uptime.log', 'a')
    if response == 0:
        file.write(f'UP: {status}')
    else:
        file.write(f'DOWN: {status}')
        downEmail()
        
    sleep(int(delay))
    send_ping_request()


send_ping_request()
