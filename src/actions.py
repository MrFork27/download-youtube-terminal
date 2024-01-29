def print_help():
    usage_string = "usage: [-h] [url]\n\n"
    info_string = "Command line application to download youtube video audios.\n\n"
    positional_arguments_string = (
        "positional arguments:\n url                 The Youtube video url\n\n"
    )
    options_string = "options:\n -h, --help          Show this help message and exit"

    print(usage_string + info_string + positional_arguments_string + options_string)


def download_audio(url):
    print(f"Downloading audio from {url}")
