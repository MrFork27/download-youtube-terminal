import unittest
import sys
import src.params as params
from unittest.mock import patch


class TestParams(unittest.TestCase):
    def test_get_param_action(self):
        help_short_arguments = ["./src/main.py", "-h"]
        help_long_arguments = ["./src/main.py", "--help"]
        audio_short_arguments = ["./src/main.py", "-a", "asdf"]
        audio_long_arguments = ["./src/main.py", "--audio", "asdf"]
        video_short_arguments = ["./src/main.py", "-v", "asdf"]
        video_long_arguments = ["./src/main.py", "--video", "asdf"]
        error_arguments = ["./src/main.py", "fdkla", "asdf"]

        with patch.object(sys, "argv", help_short_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.HELP)
        with patch.object(sys, "argv", help_long_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.HELP)
        with patch.object(sys, "argv", audio_short_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.AUDIO)
        with patch.object(sys, "argv", audio_long_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.AUDIO)
        with patch.object(sys, "argv", video_short_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.VIDEO)
        with patch.object(sys, "argv", video_long_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.VIDEO)
        with patch.object(sys, "argv", error_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.ERROR)

    def test_check_param(self):
        HELP_PARAMS = ["-h", "--help"]
        AUDIO_PARAMS = ["-a", "--audio"]
        VIDEO_PARAMS = ["-v", "--video"]
        help_short_arguments = ["./src/main.py", "-h"]
        help_long_arguments = ["./src/main.py", "--help"]
        audio_short_arguments = ["./src/main.py", "-a", "asdf"]
        audio_long_arguments = ["./src/main.py", "--audio", "asdf"]
        video_short_arguments = ["./src/main.py", "-v", "asdf"]
        video_long_arguments = ["./src/main.py", "--video", "asdf"]
        error_arguments = ["./src/main.py", "fdkla"]

        try:
            with patch.object(sys, "argv", help_short_arguments):
                params.check_param(HELP_PARAMS)
            with patch.object(sys, "argv", help_long_arguments):
                params.check_param(HELP_PARAMS)
        except:
            self.fail(f"check_param with {HELP_PARAMS} raised Exception")

        try:
            with patch.object(sys, "argv", audio_short_arguments):
                params.check_param(AUDIO_PARAMS)
            with patch.object(sys, "argv", audio_long_arguments):
                params.check_param(AUDIO_PARAMS)
        except:
            self.fail(f"check_param with {AUDIO_PARAMS} raised Exception")

        try:
            with patch.object(sys, "argv", video_short_arguments):
                params.check_param(VIDEO_PARAMS)
            with patch.object(sys, "argv", video_long_arguments):
                params.check_param(VIDEO_PARAMS)
        except:
            self.fail(f"check_param with {VIDEO_PARAMS} raised Exception")

        try:
            with patch.object(sys, "argv", error_arguments):
                params.check_param(HELP_PARAMS)
        except:
            self.fail(f"check_param with {error_arguments} raised Exception")


if __name__ == "___main___":
    unittest.main()
