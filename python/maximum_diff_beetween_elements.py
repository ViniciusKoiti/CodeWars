def maximum_diff_beetween_elements(arr):
    
    min_diff = float('inf')
    max_diff = -1
    
    for i in range(len(arr)):
        if min_diff > arr[i]:
            min_diff = arr[i]
        diff = arr[i] - min_diff
        
        if diff > max_diff:
            max_diff = diff
    return max_diff if max_diff > 0 else -1

test_cases = {
    "Test 1": [7, 1, 5, 4],   
    "Test 2": [9, 4, 3, 2],    
    "Test 3": [1, 5, 2, 10],  
    "Test 4": [4, 3, 2, 6, 8], 
    "Test 5": [3, 3, 3],      
}

results = {key: maximum_diff_beetween_elements(value) for key, value in test_cases.items()}
print(results)