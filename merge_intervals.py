def merge_intervals(arr):
    # Sort Array by starting times
    arr.sort(key=lambda x: x[0])

    # Instantiate an output array
    output = [arr[0]]

    # Iterate through intervals
    for interval in arr:

        # If the ending time of the last interval is before the starting time of the next interval
        if output[-1][1] < interval[0]: 
            # Add it to the output array
            output.append(interval)
        
        else:
            # Merge the intervals if there is overlap --> take the largest of the two end times
            output[-1][1] = max(output[-1][1], interval[1])
    
    # Return the merged intervals
    return output