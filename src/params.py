import enum
import sys


class ParamsType(enum.Enum):
    ERROR = 0
    HELP = 1
    AUDIO = 2
    VIDEO = 3


def get_param_action():
    HELP_PARAMS_LEN = 2
    HELP_PARAMS = ["-h", "--help"]
    AUDIO_PARAMS_LEN = 3
    AUDIO_PARAMS = ["-a", "--audio"]
    VIDEO_PARAMS = ["-v", "--video"]
    param_action = -1

    try:
        if len(sys.argv) == HELP_PARAMS_LEN:
            check_param(HELP_PARAMS)
            param_action = ParamsType.HELP
        elif len(sys.argv) == AUDIO_PARAMS_LEN:
            if check_param(AUDIO_PARAMS):
                param_action = ParamsType.AUDIO
            elif check_param(VIDEO_PARAMS):
                param_action = ParamsType.VIDEO
            else:
                raise Exception("fatal: See '--help'.")
        else:
            raise Exception("fatal: See '--help'.")
    except Exception as error:
        print(error)
        param_action = ParamsType.ERROR

    return param_action


def check_param(params_to_check):
    if not sys.argv[1] in params_to_check:
        return False

    return True
