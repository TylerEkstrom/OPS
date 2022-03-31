from operator import truediv
from time import sleep
from zipfile import ZipFile


def start():
    filepath = input('Zipfile: ')
    extract_location = input('where would you like to extract this to?')
    f = open('./rockyou.txt', 'r')
    passwords = f.readlines()
     
    for password in passwords:
      connected = attempt_to_unzip(filepath, password.rstrip(), extract_location)  
      if connected:
        sleep(5)
        return


def attempt_to_unzip(filepath:str, password: str, extract_location: str):
    try:
        with ZipFile(filepath) as f:
            print(f'Attempting to extract with {password}')
            f.extractall(extract_location, f.filelist, bytes(password, 'utf-8'))
            f.close()
            print(f'Successfully extracted with password {password}')
            return True
    except: 
        return False

