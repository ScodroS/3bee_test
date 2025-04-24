import unittest

from pollinator_abundance.handler import pollinator_abundance_calculation


class TestHandler(unittest.TestCase):
    def test_handler(self):
        """
        testing handler
        """
        result = pollinator_abundance_calculation()
        # TODO here I should check whether the output of pollinator_abundance_calculation is equal to the expected
        #  result, but all the output results are None? The results under the dict key 'result_values' are all None
        self.assertEqual(2, 1)


if __name__ == '__main__':
    unittest.main()
