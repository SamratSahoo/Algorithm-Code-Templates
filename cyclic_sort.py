# Missing Number
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        # Condition depends on the problem given
        # Range for this one is [0, len(arr)] --> the value could be equal to the length of the array and therefore "out of bounds" 
        # That's why we continue to avoid IndexOutOfBounds Errors
        if arr[i] == len(arr):
            i += 1
            continue
        
        # Get the intended correct index for where this number should go
        correctIndex = arr[i]

        # Check if the number at correctIndex and current index are the same
        if arr[correctIndex] != arr[i]: 

            # If not, swap them
            arr[correctIndex], arr[i] = arr[i], arr[correctIndex]
        
        else:
            # If they are teh same, increment i and repeat with the next set fo numbers
            i += 1

    # Iterate through the remainder of the elements
    for index, element in enumerate(arr):

        # Check if there is a mismatch between index and element
        if index != element:

            # return that index
            return index
    
    # If all elements match, then return the "base case"
    return len(arr)