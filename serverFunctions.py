def quitter():
    return "quit"


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


def get_song_list(data, album_name):
    """
    gives you a list of songs in a given album
    :param data: source
    :param album_name:
    :return: string: names of songs
    """
    if album_name in data:
        song_list = "Songs: \n"
        for song in data[album_name]["songs"]:
            song_list += song
            song_list += "\n"
        return song_list
    else:
        return "[!] album does not exist"


def get_song_length(data, song_name):
    """
    gives you a length of a song by a given name
    :param data: source
    :param song_name:
    :return: string: length of a song
    """
    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return data[album]["songs"][song]["length"]
    return "[!] Song not found"


def get_song_lyrics(data, song_name):
    """
    gives you lyrics of a song by a given name
    :param data: source
    :param song_name:
    :return: string: lyrics of a song
    """
    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return data[album]["songs"][song]["lyrics"]
    return "[!] Song not found"


def get_source_album(data, song_name):
    """
    gives you a name of album containing given song
    :param data: source
    :param song_name:
    :return: string: name of an album
    """
    for album in data:
        for song in data[album]["songs"]:
            if song == song_name:
                return album
    return "[!] Song not found"


def find_song_name(data, song_name):
    """
    gives you names of songs containing given substring
    :param data: source
    :param song_name:
    :return: string: song names
    """
    names = ""
    for album in data:
        for song in data[album]["songs"]:
            if song_name.lower() in song.lower():
                names += ("'" + song + "'" + " from album: " + album + "\n")
    if names == "":
        return "[!] Nothing found"
    return names


def find_song_lyrics(data, text):
    """
    gives you songs which lyrics contain given substring
    :param data: source
    :param text: substring
    :return: string: song names
    """
    names = ""
    for album in data:
        for song in data[album]["songs"]:
            if text.lower() in data[album]["songs"][song]["lyrics"].lower():
                names += ("'" + song + "'" + " from album: " + album + "\n")
    if names == "":
        return "[!] Nothing found"
    return names


def get_words(data):
    """
    Gives you all the words from songs
    :param data: Source
    :return: list containing all words in file
    """
    all_words = []
    for album in data:
        for song in data[album]["songs"]:
            temp = data[album]["songs"][song]["lyrics"]
            lines = temp.splitlines()
            for line in lines:
                line = line.replace(",", "")
                line = line.replace(".", "")
                line = line.strip("!")
                line = line.strip("?")
                line = line.replace("-", "")
                words = line.split(" ")
                for word in words:
                    if word != "":
                        all_words.append(word.lower())
    return all_words


def get_top_words(data, n):
    """
    Gets you a top 'n' most common words in all songs
    :param data: source
    :param n: top how many you want to get
    :return:
    """
    from collections import Counter

    words = get_words(data)
    words_to_count = (word for word in words)
    common_words = Counter(words_to_count)
    common_words = common_words.most_common(n)

    return common_words


def get_list_top_words(data, n):
    """
    Gives you a list of top 'n' most common words
    :param data:
    :param n: top how many words you want to get
    :return:
    """
    try:
        n = int(n)
    except ValueError:
        return "[!] Only numbers allowed"

    common_words = get_top_words(data, n)

    top_words = ""
    for x in range(0, len(common_words)):
        top_words += str(x + 1) + ": "
        top_words += "'" + common_words[x][0] + "'" + ", "
        top_words += "amount: " + str(common_words[x][1])
        top_words += "\n"

    return top_words


def to_time(sec):
    """
    Converts time from seconds to HH:MM:SS format
    :param sec: amount of seconds
    :return: time in HH:MM:SS format
    """
    import datetime
    return str(datetime.timedelta(seconds=sec))


def from_time(time):
    """
    Converts time from MM:SS format so seconds
    :param time: time in MM:SS format
    :return: amount of seconds
    """
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def sort_dictionary(dictionary):
    """
    Sorts a given dictionary by values (reversed)
    :param dictionary:
    :return: sorted dictionary
    """
    return sorted(((value, key) for (key, value) in dictionary.items()), reverse=True)


def get_longest_albums(data):
    """
    Gives you a top albums by length (reversed)
    :param data: source
    :return: string: top albums by length (reversed)
    """
    album_top = "Top albums by length: \n"

    albums = {}
    # get song length in seconds and sort them
    for album in data:
        length = 0
        for song in data[album]["songs"]:
            length += from_time(data[album]["songs"][song]["length"])
        albums[album] = length

    # sort the albums by length (reversed)
    albums = sort_dictionary(albums)

    # create a nice string with top albums by length
    for x in range(0, len(albums)):
        album_top += str(x + 1) + ": "
        album_top += albums[x][1] + ", "
        album_top += "length: " + to_time(albums[x][0])
        album_top += "\n"
    return album_top


def open_in_browser():
    return "[+] Successfully opened"


def download_video():
    return "[+] Video downloaded successfully"


def convert_video_to_audio():
    return "[+] Converted successfully"


