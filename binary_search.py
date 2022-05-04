# Simple Binary Search
def binary_search(arr, target):
    
    # Start variable to keep track of left pointer
    start = 0

    # End variable to keep track of right pointer
    end = len(arr) - 1

    # Traverse while the pointers have not crossed
    while start <= end:

        # Calculate middle value
        middle = start + end // 2

        # Check if middle value is equal to the target
        if arr[middle] == target:
            # Return middle index if so
            return middle

        # Check if middle is greater than target
        elif arr[middle] > target:
            # Move end pointer  to middle
            end = middle -1
        
        else:
            # Else move the start pointer to middle
            start = middle + 1

    # Return -1 if nothing is found    
    return -1
