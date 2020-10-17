import numpy as np


def knapsack(wt: list, val: list, W: int, n: int):

    """ Recursive Method for 0-1 Knapsack Problem """

    # Base Condition
    if W == 0 or n == 0:
        return 0

    #Check Storage
    if t[n][W] != -1:
        return t[n][W]

    # Choice Conditions
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    else:
        t[n][W] = knapsack(wt, val, W, n-1)
    return t[n][W]



if __name__ == '__main__':
    n, W = map(int, input().split())
    
    t = np.zeros((n+1, W+1), dtype=np.int_)-1

    wt = list(map(int, input().split()))
    val = list(map(int, input().split()))

    print(knapsack(wt, val, W, n))
