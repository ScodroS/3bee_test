import unittest


class TestHandler(unittest.TestCase):
    def test_handler(self):
        """
        test handler
        """
        # example
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
