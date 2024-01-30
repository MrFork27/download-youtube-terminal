import unittest


class TestParams(unittest.TestCase):
    def test_get_param_action(self):
        data1 = 1
        data2 = 2
        result = data1 + data2
        self.assertEqual(result, 3)


if __name__ == "___main___":
    unittest.main()
