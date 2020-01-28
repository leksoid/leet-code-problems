# Given a 32-bit signed integer, reverse digits of an integer.
import unittest


def reverse_int(input):
    numbers = [each for each in str(input)]
    result = ""
    for digit in reversed(numbers):
        result += digit
    if result.endswith("-"):
        return -int(result[:-1])
    else:
        return int(result)


class ReverseIntTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(reverse_int(123), 321)
    
    def test_negative(self):
        self.assertEqual(reverse_int(-123), -321)

    def test_ends_with_zero(self):
        self.assertEqual(reverse_int(120), 21)

if __name__ == '__main__':
    unittest.main()