import numpy as np

# arr = list(map(int, input().split()))
# s = int(input())


def n_subset_sum(arr, s):
    n = len(arr)
    t = np.zeros((n+1, s+1), dtype=np.int_)
    t[:, 0] = 1


    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return (t[-1][-1])
