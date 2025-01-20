def colors(colors):
    n = len(colors)
    left = 0
    for i in range(len(colors)):
        if colors[i] == 0:
            colors[i], colors[left] = colors[left], colors[i]
            left += 1
    
    right = n - 1
    for i in range(n - 1, -1, -1):
        if colors[i] == 2:
            colors[i], colors[right] = colors[right], colors[i]
            right -= 1
            
    return colors

def test_colors():
    # Test cases
    test_cases = [
        ([2, 0, 1], [0, 1, 2]),  # Simple case with all three values
        ([2, 0, 2, 1, 0, 1], [0, 0, 1, 1, 2, 2]),  # Mixed case
        ([0, 0, 0], [0, 0, 0]),  # All zeros
        ([1, 1, 1], [1, 1, 1]),  # All ones
        ([2, 2, 2], [2, 2, 2]),  # All twos
        ([0, 1, 2, 1, 0], [0, 0, 1, 1, 2]),  # Case with a mix starting and ending with 0
        ([], []),  # Empty list
    ]

    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        try:
            output = colors(input_data[:]) 
            assert output == expected_output, f"Test case {i} failed: input={input_data}, output={output}, expected={expected_output}"
            print(f"Test case {i} passed!")
        except AssertionError as e:
            print(e)

if __name__ == "__main__":
    test_colors()
