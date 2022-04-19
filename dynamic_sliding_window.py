# Subarray Product Less Than K: Dynamic Sliding Window
def dynamic_sliding_window(array, k):
    # Edge cases
    if k <= 1:
        return 0
    
    # Initialize left pointer, heuristic, and result
    left = 0
    product = 1
    result = 0

    # Use for loop to control the right pointer
    for right, element in enumerate(array):
        
        # Update heuristic
        product *= element
        
        # Move left pointer when certain condition is not being met 
        # This makes the sliding window dynamic
        while product >= k:

            # Update heuristic for moving the left pointer
            product /= element
            left += 1

        # Update the result based on new 
        # positions of left and right pointers
        result += right - left + 1
        
    # Return the result
    return result