import os

import passwordchecker

# creating menu

options = {
  '1': passwordchecker.start,
  'q': quit,
  'Q': quit
}


def main():
  print("""
  Please Select an option:

1 - Check Password
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
