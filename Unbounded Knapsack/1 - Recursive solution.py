def knapsack(wt: list, val: list, W: int, n: int):

    """ Recursive Method for 0-1 Knapsack Problem """

    # Base Condition
    if W == 0 or n == 0:
        return 0

    # Choice Conditions
    if wt[n-1] <= W:
        return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n), knapsack(wt, val, W, n-1))
    else:
        return knapsack(wt, val, W, n-1)

