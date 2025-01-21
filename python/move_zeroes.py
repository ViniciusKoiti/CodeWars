import unittest

def move_zeroes(arr):
    n = len(arr)
    left = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
    return arr
    
class TestMoveZeroes(unittest.TestCase):

    def test_single_zero(self):
        nums = [0]
        expected = [0]
        self.assertEqual(move_zeroes(nums), expected)

    def test_single_non_zero(self):
        nums = [1]
        expected = [1]
        self.assertEqual(move_zeroes(nums), expected)

    def test_zero_and_non_zero(self):
        nums = [0, 1]
        expected = [1, 0]
        self.assertEqual(move_zeroes(nums), expected)

    def test_multiple_zeros_and_non_zeros(self):
        nums = [1, 0, 2, 0, 3]
        expected = [1, 2, 3, 0, 0]
        self.assertEqual(move_zeroes(nums), expected)

    def test_multiple_zeros_in_sequence(self):
        nums = [4, 2, 4, 0, 0, 3, 0]
        expected = [4, 2, 4, 3, 0, 0, 0]
        self.assertEqual(move_zeroes(nums), expected)

    def test_no_zeros(self):
        nums = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(move_zeroes(nums), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(move_zeroes(nums), expected)

    def test_empty_array(self):
        nums = []
        expected = []
        self.assertEqual(move_zeroes(nums), expected)

if __name__ == "__main__":
    unittest.main()