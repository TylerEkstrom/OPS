#!/usr/env python

# this files does things
# author: Tyler 
# Last updated 11/30/2021                                                                                                          

import socket
import sys
import time

# function definition does not execute until funtion invocation

def simple_math(nums):
  total = 0 
  for item in nums:
    total += int(item)
    time.sleep(.25)
    print(" [~] running total: ", total)

  print("[+] what is the sum of your number", total)


def get_host_ip():
  host = socket.getaddrinfo(socket.gethostname(), 1)
  print(host)


def main(args):
  # do some work
  get_host_ip()
  print("done")


if __name__ == '__main__':
# function execution (invocation)
  main(sys.argv)
