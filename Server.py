"""
YOU MAY HAVE TO INSTALL FOLLOWING PACKAGES TO RUN THIS PROGRAM:
youtube-search
"""

import serverSwitches
import sys
import mySock
import serverFunctions

VERSION = "2.1"

FILE_PATH = "Pink_Floyd_DB.txt"
MESSAGE_DELIMITER = "#"
ALBUM_DELIMITER = "#"
SONG_DELIMITER = "*"
INFO_DELIMITER = "::"

PASSWORD = "1234"
HASHED_PASSWORD = hash(PASSWORD)
PASSWORD_ERROR = ""

ERROR_SIGN = "!"

INPUT_ERROR = "[!] Invalid input"
DISCONNECTED_ERROR = "[!] Client disconnected\n"
LOGIN_SUCCESS = "[+] Login successful"
ATTEMPT_ERROR = "[!] maximum amount of attempts reached\n"
ATTEMPTS_LEFT = "[!] Wrong password, you have %d attempts left\n"


def execute():
    import os
    os.system('cmd /c "pip install youtube-search"')


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


def extractor(file_path):
    """
    Extracts data from file in 'file_path' and
    separates it into dictionaries of dictionaries of dictionaries
    :param file_path: a file
    :return: data in a human readable format
    """
    with open(file_path, "r") as DB:
        lines = DB.read()
        lines = lines[1:]

        lines = lines.split(ALBUM_DELIMITER)

        albums = []
        for album in lines:
            albums.append(album.split(SONG_DELIMITER))

        # get albums
        data = {}
        for album in albums:
            album_info = {}
            album_data = album[0].split(INFO_DELIMITER)
            album_info["date"] = album_data[1]

            # get data for each song
            songs = {}
            for x in range(1, len(album)):
                song = {}
                song_data = album[x].split(INFO_DELIMITER)
                song["singer"] = song_data[1]
                song["length"] = song_data[2]
                song["lyrics"] = song_data[3]
                songs[song_data[0]] = song

            album_info["songs"] = songs

            data[album_data[0]] = album_info

        return data


def get_album_list(data):
    """
    takes all keys of 'data' dictionary
    and returns them (returns names of albums)
    :param data: source
    :return: string that represents album list
    """
    albums_list = "Album list: \n"
    for album_name in data:
        albums_list += album_name
        albums_list += "\n"

    return albums_list


def switch(i, data, user_input):
    """
    Simple switch case implementation in python
    that performs one of functions and returns output
    :param i: switch parameter
    :param data: source
    :param user_input:
    :return: data for user
    """
    switcher = {
        0: serverFunctions.quitter(),
        1: get_album_list(data),
        2: serverFunctions.get_song_list(data, user_input),
        3: serverSwitches.logic(data, user_input, serverSwitches.song_info_switch),
        4: serverSwitches.logic(data, user_input, serverSwitches.find_switch),
        5: serverSwitches.logic(data, user_input, serverSwitches.stat_switch),
        6: serverFunctions.open_in_browser(),
        7: serverFunctions.download_video(),
        8: serverFunctions.convert_video_to_audio()
    }
    return switcher.get(i, INPUT_ERROR)


def create_message(client_msg, data):
    """
    Creates a message for user based on his inpur
    :param client_msg: message received from client
    :param data: source
    :return: created message
    """

    try:
        choice = int(client_msg[0])
    except ValueError:
        print(INPUT_ERROR)
    user_input = client_msg[1]

    msg = switch(choice, data, user_input)

    return msg


def login(client_soc):
    """
    Performs a login process
    :param client_soc:
    :return: login result
    """
    attempts = 5

    while True:
        # check if client suddenly left
        try:
            client_msg = client_soc.recv(2048).decode()
        except ConnectionError:
            return DISCONNECTED_ERROR

        if hash(client_msg) == HASHED_PASSWORD:
            # tell the client that password is correct
            client_soc.send(LOGIN_SUCCESS.encode())
            return LOGIN_SUCCESS

        # attempt counter
        attempts -= 1
        if attempts == 0:
            client_soc.send(ATTEMPT_ERROR.encode())
            break

        # send number of attempts left
        client_soc.send((ATTEMPTS_LEFT % attempts).encode())

    return ATTEMPT_ERROR


def main():
    hello()

    installer()

    # Try to get data from file
    try:
        data = extractor(FILE_PATH)
        print("[+] Source file opened")
    except FileNotFoundError:
        print("[!] File not found")
        sys.exit()

    while True:
        # Establish connection
        client_soc, client_address, listening_sock = mySock.server()

        # login process
        login_info = login(client_soc)
        if login_info[1] == ERROR_SIGN:
            print(login_info)
            mySock.closer(listening_sock, client_soc)
            continue
        else:
            print(login_info)

        # message exchange process
        while True:
            # Check if client suddenly disconnected
            try:
                client_msg = client_soc.recv(2048).decode()
            except ConnectionError:
                break

            # Split param from data
            client_msg = client_msg.split(MESSAGE_DELIMITER)
            print(client_msg)

            # Create a message for user
            msg = create_message(client_msg, data)

            print("msg:" + msg)

            if msg == "quit":
                break

            client_soc.send(msg.encode())

        # Close the connection
        mySock.closer(listening_sock, client_soc)


if __name__ == '__main__':
    main()
