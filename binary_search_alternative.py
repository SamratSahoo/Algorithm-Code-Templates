def binary_search(n, nums):
    def condition(threshold):
        #Example condition function
        sm = 0
        for num in nums:
            sm += math.ceil(num / divisor)
        return sm <= threshold
    
    #one of the three things that need to be changed are l and r values
    left = 1
    right = max(nums)

    #loop terminating condition
    while left < right:
        #calculate the mid value for binary search
        mid = left + (right - left) // 2 # avoid overflow

        #condition function for each problem is unique
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    #third thing that changes, return left or left - 1 depending on the problem
    return left 
    #or return right, they are both the same after the loop terminates

