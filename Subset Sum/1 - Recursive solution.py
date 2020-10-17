def is_subset_sum(arr, s, index=0):
    if s == 0:
        return True

    if index >= len(arr):
        return False

    if arr[index] <= s:
        return subset_sum(arr, s-arr[index], index+1) or subset_sum(arr, s, index+1)
    else:
        return subset_sum(arr, s, index+1)

    

    
