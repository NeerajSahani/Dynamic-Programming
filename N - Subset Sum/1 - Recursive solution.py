def n_subset_sum(arr, s, index=0):
    if s == 0:
        return 1

    if index >= len(arr):
        return 0

    if arr[index] <= s:
        return n_subset_sum(arr, s-arr[index], index+1) + n_subset_sum(arr, s, index+1)
    else:
        return n_subset_sum(arr, s, index+1)

    

    
