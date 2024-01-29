import enum
import sys


class ParamsType(enum.Enum):
    ERROR = 0
    HELP = 1
    URL = 2


def get_param_action():
    HELP_PARAMS_LEN = 2
    HELP_PARAMS = ["-h", "--help"]
    URL_PARAMS_LEN = 3
    URL_PARAMS = ["url"]
    param_action = -1

    try:
        if len(sys.argv) == HELP_PARAMS_LEN:
            check_param(HELP_PARAMS)
            param_action = ParamsType.HELP
        elif len(sys.argv) == URL_PARAMS_LEN:
            check_param(URL_PARAMS)
            param_action = ParamsType.URL
        else:
            raise Exception("fatal: See '--help'.")
    except Exception as error:
        print(error)
        param_action = ParamsType.ERROR

    return param_action


def check_param(params_to_check):
    if not sys.argv[1] in params_to_check:
        raise Exception("fatal: See '--help'.")
