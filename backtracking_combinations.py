# Subsets
def backtracking_combinations(nums):
    
    # Answer Array to keep track of all combinations
    ans = []
    
    def backtrack(current, index):
        # Add current subset to the answer
        ans.append(list(current))

        # Iterate through remainder of decision space
        for i in range(index, len(nums)):
            
            # Add a decision to current subset
            current.append(nums[i])

            # Backtrack with new decision space
            backtrack(current, i+1)

            # Remove last deicison to add a new decision on next loop cycle
            current.pop()

    # Call the backtrack method
    backtrack([], 0)

    # Return the answer
    return ans

