from collections import UserList
from time import sleep

import pwnedpasswords


def passList():
  useList = input("Use your own list? Y/N? ")
  if useList == 'Y':
    f = open('./rockyou.txt', 'r')
    passwords = f.read()
    return passwords
  #if useList =='N':
    

passwords = passList()

def check_password(passwordToBeChecked: str):
  print(passwordToBeChecked)
  lowered = passwordToBeChecked.lower()
  if passwords and lowered in passwords:
    print('--Checking passwords--')
    print('That is a known passowrd don\'t use it!')
    sleep(3)
    return
  print('-- Checking against PWNEDPASSWORDS DB --')
  found = pwnedpasswords.check(lowered)
  if found:
        print('That is a known passowrd don\'t use it!')
  else:
    print('That is an unknown password')

  sleep(3)

def start():
    print("""
   TODO PASSWORD_CHECKER BANNER HERE
    """)
    password = input('Password:')
    check_password(password)
    print('something else')

