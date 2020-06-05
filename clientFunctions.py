INPUT_ERROR = "[!] Invalid input"
NUMBER_ERROR = "[!] Only numbers allowed"


def get_input(local_switch):
    """
    Gets input from user and checks it
    :return:
    """
    data = INPUT_ERROR

    while data == INPUT_ERROR:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(NUMBER_ERROR)
            continue

        data = local_switch(choice)

    return str(choice), data


def quitter():
    return "quit"


def album_list():
    return ""


def song_list():
    album_name = input("Enter album name to display the list of songs from: ")
    return album_name


def song_length():
    song_name = input("Enter song name: ")
    return song_name


def song_lyrics():
    song_name = input("Enter song name: ")
    return song_name


def source_album():
    song_name = input("Enter song name: ")
    return song_name


def find_song_name():
    song_name = input("Enter song name: ")
    return song_name


def find_song_lyrics():
    text = input("Enter lyrics: ")
    return text


def get_top_frequent_words():
    number = input("Enter top how many words you want to get: ")
    return number


def get_top_longest_albums():
    return ""


def get_song_link_youtube(song_name):
    print(song_name)
    """
    Takes a song name and returns a link to a youtube video with a given song
    :param song_name:
    :return: link to a video with given song
    """
    try:
        from youtube_search import YoutubeSearch
    except:
        print("[!] Please install required modules")
        exit()

    results = YoutubeSearch("pink floyd " + song_name, max_results=1).to_dict()

    return "https://www.youtube.com/" + results[0]["link"]


def get_playlist_link_youtube(album_name):
    """
    Takes name of an music album and returns youtube link to is
    :param album_name:
    :return:
    """
    try:
        from youtube_search import YoutubeSearch
    except:
        print("[!] Please install required modules")
        exit()

    results = YoutubeSearch("pink floyd " + album_name + " playlist", max_results=1).to_dict()

    return "https://www.youtube.com/" + results[0]["link"]


def open_playlist_video():
    """
    Opens a playlist in browser
    :return:
    """
    import webbrowser

    album_name = input("Enter album name to open: ")
    url = get_playlist_link_youtube(album_name)
    webbrowser.open(url)

    return ""


def open_song_video():
    """
    Opens a video in browser
    :return:
    """
    import webbrowser

    song_name = input("Enter name of song to open: ")
    url = get_song_link_youtube(song_name)
    webbrowser.open(url)

    return ""


def download_video():
    """
    Downloads video at a given url
    :return: name of downloaded song
    """
    from pytube import YouTube

    song_name = input("Enter name of a song: ")
    video_url = get_song_link_youtube(song_name)

    video = YouTube(video_url)

    video = video.streams.get_highest_resolution()
    video.download()
    return ""


def convert_video_to_audio():
    """
    Converts all video to audio
    :return:
    """
    import os

    VIDEOS_EXTENSION = '.mp4'  # for example
    AUDIO_EXT = 'wav'

    EXTRACT_VIDEO_COMMAND = ('ffmpeg\\bin\\ffmpeg.exe -y -i "{from_video_path}" '
                             '-f {audio_ext} -ab 192000 '
                             '-vn "{to_audio_path}"')

    files = os.listdir()

    for f in files:
        if f.endswith(VIDEOS_EXTENSION):
            audio_file_name = '{}.{}'.format(f, AUDIO_EXT)
            command = EXTRACT_VIDEO_COMMAND.format(
                from_video_path=f, audio_ext=AUDIO_EXT, to_audio_path=audio_file_name,
            )
            os.system(command)

    return ""


