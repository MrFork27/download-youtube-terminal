import enum
import sys


class Params(enum.Enum):
    ERROR = 0
    HELP = 1
    URL = 2


def get_param_action():
    HELP_PARAMS_LEN = 2
    URL_PARAMS_LEN = 3
    param_action = -1

    try:
        if len(sys.argv) == HELP_PARAMS_LEN:
            check_help_param()
            param_action = Params.HELP
        elif len(sys.argv) == URL_PARAMS_LEN:
            check_url_param()
            param_action = Params.URL
        else:
            raise Exception("fatal: See '--help'.")
    except Exception as error:
        print(error)
        param_action = Params.ERROR

    return param_action


def check_help_param():
    HELP_PARAMS = ["-h", "--help"]

    if not sys.argv[1] in HELP_PARAMS:
        raise Exception("fatal: See '--help'.")


def check_url_param():
    URL_PARAMS = ["url"]

    if not sys.argv[1] in URL_PARAMS:
        raise Exception("fatal: See '--help'.")
