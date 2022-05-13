# Permutations
def backtracking_permutation(nums):
    # Visited set to ensure we do not add the same element twice
    # In combinations, this is handled by the for loop since the decision space decreases with each element
    # With permutations, we need this because the whole decision space is available with each element
    visited = set()
    
    # Answer to hold the answers
    ans = []
        
    def backtrack(visited, current):
        # if the length of the current array is equal to the length of the nums array
        if len(current) == len(nums):
            ans.append(list(current))
        
        # Iterate through the entire decision space
        for i in range(len(nums)):
            # Check if the index being analyzed has already been added to the current permutation
            if i not in visited:

                # If not, add it to the visited list
                visited.add(i)

                # Add the element at that index to the permutation
                current.append(nums[i])

                # Backtrack with new constraints
                backtrack(visited, current)

                # Remove last deicison to add a new decision on next loop cycle
                current.pop()

                # Remove index from the visited list since its not longer in the permutation
                visited.remove(i)
    
    # Call with empty visited
    backtrack(visited, [])

    # Return the answer
    return ans