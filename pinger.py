import datetime
import os
from time import sleep

host = input('What is the IP? ')
delay = input('How often do you want to check the host (seconds)? ')
emailTo =  input('In the event that the server goes down what email would you like to have notified? ')


def send_ping_request():
    currentTime = datetime.datetime.now()
    response = os.system('ping ' + host)
    status = f'{currentTime} - {host}\n'
    file = open('uptime.log', 'a')
    if response == 0:
        file.write(f'UP: {status}')
    else:
        file.write(f'DOWN:  {status}')
    sleep(int(delay))
    send_ping_request()


send_ping_request()
