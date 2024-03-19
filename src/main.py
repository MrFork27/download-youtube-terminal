import actions
import sys
from params import ParamsType, get_param_action


def main():
    ACTION = get_param_action()

    if ACTION == ParamsType.HELP:
        actions.print_help()
    elif ACTION == ParamsType.AUDIO:
        actions.download_audio(sys.argv[2])
    elif ACTION == ParamsType.VIDEO:
        actions.download_video(sys.argv[2])


if __name__ == "__main__":
    main()
