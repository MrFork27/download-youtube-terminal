import unittest
import sys
import src.params as params
from unittest.mock import patch


class TestParams(unittest.TestCase):
    def test_get_param_action(self):
        help_short_arguments = ["./src/main.py", "-h"]
        help_long_arguments = ["./src/main.py", "--help"]
        url_short_arguments = ["./src/main.py", "-u", "asdf"]
        url_long_arguments = ["./src/main.py", "--url", "asdf"]
        error_arguments = ["./src/main.py", "fdkla", "asdf"]

        with patch.object(sys, "argv", help_short_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.HELP)
        with patch.object(sys, "argv", help_long_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.HELP)
        with patch.object(sys, "argv", url_short_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.URL)
        with patch.object(sys, "argv", url_long_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.URL)
        with patch.object(sys, "argv", error_arguments):
            param_action = params.get_param_action()
            self.assertEqual(param_action, params.ParamsType.ERROR)


if __name__ == "___main___":
    unittest.main()
