import unittest
import inclusive_range

class TestInclusiveRange(unittest.TestCase):

    def test_single_integer(self):

        s="10"
        result=inclusive_range.range_string_to_inclusive_integer_range(s)

        # the expected is always 1+end (to be inclusive)
        expected=range(10,11)
        self.assertEqual(result, expected, f"failed on {s}")

    def test_single_integer_with_leading_zero(self):

        s="05"
        result=inclusive_range.range_string_to_inclusive_integer_range(s)

        # the expected is always 1+end (to be inclusive)
        expected=range(5,6)
        self.assertEqual(result, expected, f"failed on {s}")

    def test_range_integer_with_leading_zeros(self):

        s="08-11"
        result=inclusive_range.range_string_to_inclusive_integer_range(s)

        # the expected is always 1+end (to be inclusive)
        expected=range(8,12)
        self.assertEqual(result, expected, f"failed on {s}")

    def test_range_integer(self):

        s="8-11"
        result=inclusive_range.range_string_to_inclusive_integer_range(s)

        # the expected is always 1+end (to be inclusive)
        expected=range(8,12)
        self.assertEqual(result, expected, f"failed on {s}")


if __name__ == '__main__':
    unittest.main()
