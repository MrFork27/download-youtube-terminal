import os
from pytube import YouTube


def print_help():
    usage_string = "usage: [-h] [-u URL]\n\n"
    info_string = "Command line application to download youtube video audios.\n\n"
    url_param_info = (
        "options:\n -u [URL], --url [URL]          Show this help message and exit"
    )
    help_param_info = (
        "options:\n -h, --help                     Show this help message and exit"
    )

    print(usage_string + info_string + url_param_info + help_param_info)


def download_audio(url):
    AUDIO_FORMAT = ".mp3"
    MUSIC_DIRECTORY = "./music/"
    try:
        yt = YouTube(url)
        print(f"Downloading audio from {yt.title}")
        audio_streams = yt.streams.filter(only_audio=True).first()

        audio_file = audio_streams.download(output_path=MUSIC_DIRECTORY)
        song_name = os.path.splitext(audio_file)[0]
        new_file = song_name + AUDIO_FORMAT
        os.rename(audio_file, new_file)

    except Exception as error:
        print(error.__class__)
        print(error)
