import os
from tkinter import Y

import passwordchecker
import sshAttacker
import zipper

# creating menu

options = {
  '1': passwordchecker.start,
  '2': sshAttacker.start,
  '3': zipper.start,
  'q': quit,
  'Q': quit
}


def main():
  print("""
  Please Select an option:

1 - Check Password
2 - SSH Attacker
3 - Unzipper
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
