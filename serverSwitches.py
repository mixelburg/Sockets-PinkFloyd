import serverFunctions

INPUT_ERROR = "[!] Switch Invalid input"

DELIMITER = "*"


def logic(data, user_input, chosen_switch):
    user_data = user_input.split(DELIMITER)

    print(user_data)
    try:
        choice = int(user_data[0])
    except ValueError:
        print(INPUT_ERROR)

    if len(user_data) > 1:
        param = user_data[1]
        ans = chosen_switch(choice, data, param)

        return ans


def song_info_switch(i, data, param):
    switcher = {
        1: serverFunctions.get_song_length(data, param),
        2: serverFunctions.get_song_lyrics(data, param),
        3: serverFunctions.get_source_album(data, param)
    }
    return switcher.get(i, INPUT_ERROR)


def find_switch(i, data, param):
    switcher = {
        1: serverFunctions.find_song_name(data, param),
        2: serverFunctions.find_song_lyrics(data, param)
    }
    return switcher.get(i, INPUT_ERROR)


def stat_switch(i, data, param):
    switcher = {
        1: serverFunctions.get_list_top_words(data, param),
        2: serverFunctions.get_longest_albums(data)
    }
    return switcher.get(i, INPUT_ERROR)



