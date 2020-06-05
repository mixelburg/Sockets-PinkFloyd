"""
YOU MAY HAVE TO INSTALL FOLLOWING PACKAGES TO RUN THIS PROGRAM:
youtube-search
"""

import mySock
import clientSwitches
import clientFunctions

VERSION = "2.1"

INPUT_ERROR = "[!] Invalid input"
NUMBER_ERROR = "[!] Only numbers allowed"

DELIMITER = "#"
LOGIN_SUCCESS = "[+] Login successful"
ATTEMPT_ERROR = "[!] maximum amount of attempts reached\n"


def execute():
    import os
    os.system('cmd /c "pip install youtube-search"')
    os.system('cmd /c "pip install pytube3"')


def installer():
    print("""
        Would you like to install required libraries? 
        """)
    ch = input("Enter 'y' or 'n': ")
    if ch == "y":
        execute()


def hello():
    """
    Simple hello function
    :return: none
    """
    print(("""
              _                          
             | |                         
__      _____| | ___ ___  _ __ ___   ___ 
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \\
 \ V  V /  __/ | (_| (_) | | | | | |  __/
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

  Created by mixelburg                   
  version: %s                                 
    """) % VERSION)


def menu():
    """
    Prints menu for a user
    :return: none
    """
    print("""
    You have several options:
    0: Quit
    1: Get list of albums
    2: Get song list from album
    3: Get song info 
    4: Find song
    5: Get some statistics
    6: Open song or Album playlist in YouTube
    7: Download clip or album from youtube
    8: Convert video to audio
    """)


def main_switch(i):
    """
    Simple switch case implementation in python
    :param i: switch param
    :return:
    """
    switcher = {
        0: lambda: "quit",
        1: clientFunctions.album_list,
        2: clientFunctions.song_list,
        3: clientSwitches.song_info,
        4: clientSwitches.finders,
        5: clientSwitches.stats,
        6: clientSwitches.open_in_browser,
        7: clientFunctions.download_video,
        8: clientFunctions.convert_video_to_audio,
    }
    func = switcher.get(i, lambda: INPUT_ERROR)
    return func()


def login(sock):
    """
    Prompts user to sogin
    :param sock: socket
    :return:
    """
    server_msg = ""
    while server_msg != LOGIN_SUCCESS:
        password = input("Enter a password: ")
        sock.send(password.encode())
        server_msg = sock.recv(2048).decode()
        print(server_msg)

        if server_msg == ATTEMPT_ERROR:
            sock.close()
            exit()


def main():
    hello()

    installer()

    # establish connection
    sock = mySock.client()

    menu()

    login(sock)

    while True:
        choice, data = clientFunctions.get_input(main_switch)

        # create a message for client
        msg = choice + DELIMITER + data
        sock.send(msg.encode())

        if data == "quit":
            break

        server_msg = sock.recv(2048)
        print(server_msg.decode())

    sock.close()


if __name__ == '__main__':
    main()
