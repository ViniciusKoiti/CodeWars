import unittest

def remove_duplicates(arr):
    if not arr:
        return 0
    
    position = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[position]:
            position += 1
            arr[position] = arr[i]
            
    return position + 1 
            
class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_array(self):
        nums = []
        expected_length = 0
        self.assertEqual(remove_duplicates(nums), expected_length)

    def test_single_element(self):
        nums = [1]
        expected_length = 1
        self.assertEqual(remove_duplicates(nums), expected_length)
        self.assertEqual(nums[:expected_length], [1])

    def test_no_duplicates(self):
        nums = [1, 2, 3]
        expected_length = 3
        self.assertEqual(remove_duplicates(nums), expected_length)
        self.assertEqual(nums[:expected_length], [1, 2, 3])

    def test_with_duplicates(self):
        nums = [1, 1, 2]
        expected_length = 2
        self.assertEqual(remove_duplicates(nums), expected_length)
        self.assertEqual(nums[:expected_length], [1, 2])

    def test_multiple_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3]
        expected_length = 4
        self.assertEqual(remove_duplicates(nums), expected_length)
        self.assertEqual(nums[:expected_length], [0, 1, 2, 3])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2]
        expected_length = 1
        self.assertEqual(remove_duplicates(nums), expected_length)
        self.assertEqual(nums[:expected_length], [2])

if __name__ == "__main__":
    unittest.main()            