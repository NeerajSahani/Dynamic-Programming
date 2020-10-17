import numpy as np

def n_subset_sum(arr, s, n=0):
    if s == 0:
        return True

    if n == len(arr):
        return False

    if t[n][s] != -1:
        return t[n][s]
    
    if arr[n] <= s:
        t[n][s] = n_subset_sum(arr, s-arr[n], n+1) + n_subset_sum(arr, s, n+1)
    else:
        t[n][s] = n_subset_sum(arr, s, n+1)
    return t[n][s]

    

    
if __name__ == '__main__':
    
    arr = list(map(int, input().split()))
    s = int(input())
    n = len(arr)
    t = np.zeros((n+1, s+1), dtype=np.int_)-1
    t[:, 0] = 1
    

    print(n_subset_sum(arr, s))
