# Maximum Sum of Window Size K: Fixed Sliding Window
def fixed_sliding_window(array, k):
    # Initialize left and right bounds
    left = 0
    right = k

    # Some value used as a heuristic for sliding window
    sum_of_numbers = sum(array[left:right])
    
    # Some global value to keep track of
    max_sum = float('-inf')

    # While loop to go through all subarrays with size k
    while right < len(array):
        
        # Update heuristic with value @ right pointer
        sum_of_numbers += array[right]

        # Update Global Value
        max_sum = max(max_sum, sum_of_numbers)
        
        # Update heuristic
        sum_of_numbers -= array[left]

        # Slide Window
        left += 1
        right += 1
    
    # Return the global value
    return max_sum
