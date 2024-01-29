import sys


def check_params():
    HELP_PARAMS_LEN = 2
    URL_PARAMS_LEN = 3
    URL_PARAMS = ["url"]

    try:
        if len(sys.argv) == HELP_PARAMS_LEN:
            check_help()
        elif len(sys.argv) == URL_PARAMS_LEN:
            if not sys.argv[1] in URL_PARAMS:
                raise Exception("fatal: See '--help'.")
        else:
            raise Exception("fatal: See '--help'.")
    except Exception as error:
        print(error)


def check_help():
    HELP_PARAMS = ["-h", "--help"]

    try:
        if sys.argv[1] in HELP_PARAMS:
            print_help()
        else:
            raise Exception("fatal: See '--help'.")
    except Exception as error:
        print(error)


def print_help():
    usage_string = "usage: [-h] [url]\n\n"
    info_string = "Command line application to download youtube video audios.\n\n"
    positional_arguments_string = (
        "positional arguments:\n url                 The Youtube video url\n\n"
    )
    options_string = "options:\n -h, --help          Show this help message and exit"

    print(usage_string + info_string + positional_arguments_string + options_string)
