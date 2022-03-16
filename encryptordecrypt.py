import os
from importlib.resources import path
from os.path import exists
from posixpath import dirname
from time import sleep

import clipboard as pc
from cryptography.fernet import Fernet


def menu():
    choice = input("""
     .--------.
    / .------. \\
   / /        \\ \\
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | NOPE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'

What would you like to do
  1 - Encrypt File
  2 - Decrypt File
  3 - Encrypt Message
  4 - Decrypt Message
  5 - Encrypt Folder
  6 - Decrypt Folder
  7 - Quit

  Please select a number: """)

    if choice == '1':
       print("Encypt file")
       filePath = input("Choose file to Encypt: ")
       if exists(filePath):
           Encrypt_file(filePath)
       else:
            print("[!] invalid file try again [!]")
    elif choice == '2':
      print("Decrypt File")
      filePath = input("Choose file to Decypt: ")
      if exists(filePath):
          Decrypt_file(filePath)
      else:
          print("[!] invalid file try again [!]")
    elif choice == '3':
        message = input("What is the message?: ")
        encrypt_message(message.encode())
    elif choice == '4':
        message = input("What is the encypted message?: ")
        decrypt_message(message.encode())
    elif choice == '5':
        print('Encrypt Folder')
        dirname = input('Choose a folder: ')
        encrypt_folder(dirname)
    elif choice == '6': 
        print('Decrypt Folder') 
        dirname = input('Choose a folder: ')
        decrypt_folder(dirname)
    elif choice == '7':
        shutDown()
    sleep(3)
    os.system('clear')
    menu()

def shutDown():
    print('computer self destruction in...')
    sleep(1)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    os.system('clear')
    exit(1)

def Decrypt_file(filePath):
    print("Decrypting...")
    file = open(filePath, 'rb')
    contents = file.read()
    file.close()
    decrypted_message = decrypt_message(contents)
    file = open(filePath, 'wb')
    file.write(decrypted_message.encode())
    file.close()

def Encrypt_file(filePath):
    print("Encrypting...")
    file = open(filePath, 'rb')
    contents = file.read()
    file.close()
    encrypted_message = encrypt_message(contents)
    file =  open(filePath, 'wb')
    file.write(encrypted_message.encode())
    file.close()

def load_or_generate_key():
    key_exists = exists('secret.key')

    if key_exists:
        loaded_key = open('secret.key', 'rb').read()
        cryptoligist = Fernet(loaded_key)
    else:
        key = Fernet.generate_key()
        file = open('secret.key', 'wb')
        file.write(key)
        print('key generated')
        cryptoligist = Fernet(key)
    return cryptoligist

def encrypt_message(message):
    encrypted_message = (cryptoligist.encrypt(message)).decode()
    pc.copy(encrypted_message)
    print(f"""-------------encrypted_message----------
{encrypted_message}
    """)
    return encrypted_message
    
def decrypt_message(message):
    decrypted_message = (cryptoligist.decrypt(message)).decode()
    pc.copy(decrypted_message)
    print(f"{decrypted_message}")
    return decrypted_message

def encrypt_folder(dirname):
    for path, dirnames, files in os.walk(dirname):
        for file in files:
            filePath = os.path.join(path, file)
            print(f'Encrypting File {filePath}')
            Encrypt_file(filePath)

def decrypt_folder(dirname):
    for path, dirnames, files in os.walk(dirname):
     for file in files:
         filePath = os.path.join(path, file)
         print(f'Decrypting File {filePath}')
         Decrypt_file(filePath)

cryptoligist = load_or_generate_key()
menu()
