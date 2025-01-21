def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if(arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            left = mid + 1
        elif(arr[mid] > target):
            right = mid - 1

    return -1

test_cases = {
    "Test 1": ([1, 2, 3, 4, 5], 3),   # Expected output: 2 (index of 3)
    "Test 2": ([1, 2, 3, 4, 5], 6),   # Expected output: -1 (not found)
    "Test 3": ([10, 20, 30, 40, 50], 40), # Expected output: 3 (index of 40)
    "Test 4": ([1, 3, 5, 7, 9], 7),   # Expected output: 3 (index of 7)
    "Test 5": ([], 1),                # Expected output: -1 (empty array)
}

results = {key: binary_search(arr, target) for key, (arr, target) in test_cases.items()}
print(results)