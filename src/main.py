import actions
import sys
from params import Params, get_param_action


def main():
    ACTION = get_param_action()

    if ACTION == Params.HELP:
        actions.print_help()
    elif ACTION == Params.URL:
        actions.download_audio(sys.argv[2])


if __name__ == "__main__":
    main()
