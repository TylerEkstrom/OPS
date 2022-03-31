import os
from tkinter import Y

import passwordchecker
import sshAttacker

# creating menu

options = {
  '1': passwordchecker.start,
  '2': sshAttacker.start,
  'q': quit,
  'Q': quit
}


def main():
  print("""
  Please Select an option:

1 - Check Password
2 - SSH Attacker
Q - Quit
  """)
  choice = input("> " )
  if choice in options:
    options[choice]()
  else:
    print("Invalid Option")
    os.system('cls')
  main()

def quit():
  print('quitting...')
  exit(0)

main()
