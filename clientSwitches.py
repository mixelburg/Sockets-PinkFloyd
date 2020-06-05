import clientFunctions

DELIMITER = "*"


def song_info():
    print("""
            Enter 1 to get song length 
            Enter 2 to get song lyrics
            Enter 3 to get song source album
            """)
    choice, data = clientFunctions.get_input(song_info_switch)
    return choice + DELIMITER + data


def song_info_switch(i):
    switcher = {
        1: clientFunctions.song_length,
        2: clientFunctions.song_lyrics,
        3: clientFunctions.source_album
    }
    func = switcher.get(i, lambda: clientFunctions.INPUT_ERROR)
    return func()


def finders():
    print("""
        Enter 1 to find song by name
        Enter 2 to find song by lyrics
        """)
    choice, data = clientFunctions.get_input(finders_switch)
    return choice + DELIMITER + data


def finders_switch(i):
    switcher = {
        1: clientFunctions.find_song_name,
        2: clientFunctions.find_song_lyrics
    }
    func = switcher.get(i, lambda: clientFunctions.INPUT_ERROR)
    return func()


def stats():
    print("""
    Enter 1 to get top 'n' frequent words
    Enter 2 to get top top longest albums
    """)
    choice, data = clientFunctions.get_input(stat_switch)
    return choice + DELIMITER + data


def stat_switch(i):
    """
    Simple switch case implementation in python
    :param i: switch param
    :return:
    """
    switcher = {
        1: clientFunctions.get_top_frequent_words,
        2: clientFunctions.get_top_longest_albums
    }
    func = switcher.get(i, lambda: clientFunctions.INPUT_ERROR)
    return func()


def open_in_browser():
    print("""
    Enter '1' to open a song
    Enter '2' to open an album playlist
    """)
    choice, data = clientFunctions.get_input(open_browser_switch)
    return data


def open_browser_switch(i):
    """
    Simple switch case implementation in python
    :param i: switch param
    :return:
    """
    switcher = {
        1: clientFunctions.open_song_video,
        2: clientFunctions.open_playlist_video
    }
    func = switcher.get(i, lambda: clientFunctions.INPUT_ERROR)
    return func()

