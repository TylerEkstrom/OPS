#checks password list

from time import sleep


def passList():
  f = open('./rockyou-min.txt', 'r')
  passwords = f.read()
  return passwords

passwords = passList()

def check_password(passwordToBeChecked: str):
  print('--checking password--')
  print(passwordToBeChecked)
  lowered = passwordToBeChecked.lower()
  if lowered in passwords:
    print('That is a known passowrd don\'t use it!')
  else:
    print('That is an unknown password')

  sleep(3)

def start():
    print("""
   TODO PASSWORD_CHECKER BANNER HERE
    """)
    pList = input('Password:')
    check_password(passwords)
    print('something else')

