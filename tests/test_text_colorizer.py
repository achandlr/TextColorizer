import unittest
import numpy as np
from TextColorizer import TextColorizer

class TestTextColorizer(unittest.TestCase):
    def setUp(self):
        self.tokens = ["The", " ", "quick", " ", "brown", " ", "fox", " ", "jumps", " ", "over", " ", "the", " ", "lazy", " ", "dog"]
        self.data_dict = {
            'variance': list(np.random.rand(len(self.tokens))),
            'diff_from_empty_str': list(np.random.rand(len(self.tokens)))
        }
        self.colorizer = TextColorizer(self.tokens, self.data_dict)

    def test_normalize(self):
        # Normal case
        self.assertEqual(self.colorizer.normalize([0, 5, 10]), [0.0, 0.5, 1.0])

        # All values are the same
        self.assertEqual(self.colorizer.normalize([5, 5, 5]), [0.0, 0.0, 0.0])

        # Negative values
        self.assertEqual(self.colorizer.normalize([-10, 0, 10]), [0.0, 0.5, 1.0])

    def test_colorize(self):
        # It's hard to test the specific HTML output, but you can at least check that it doesn't error out and that it returns a string
        s = self.colorizer.colorize()
        self.assertIsInstance(s, str)

        # Test case where tokens are empty
        empty_colorizer = TextColorizer([], {})
        s = empty_colorizer.colorize()
        self.assertIsInstance(s, str)
        self.assertEqual(s, "'variance':<br><br>'diff_from_empty_str': ")

if __name__ == '__main__':
    unittest.main()
