import os
from time import sleep

f = open("test.txt","w")
f.write("""test 1
test 2
test 3
""")
f.close()

f = open("test.txt", "r")
print(f.readline())

f.close()

sleep(5)

os.remove("test.txt")
