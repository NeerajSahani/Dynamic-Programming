import numpy as np


n, W = map(int, input().split())    

wt = list(map(int, input().split()))
val = list(map(int, input().split()))

t = np.zeros((n+1, W+1), dtype=np.int_)

for i in range(1, n+1):
    for j in range(1, W+1):
        if wt[i-1] <= j:
            t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
        else:
            t[i][j] = t[i-1][j]

print(t[-1][-1])
