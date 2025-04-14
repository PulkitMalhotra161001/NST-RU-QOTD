https://my.newtonschool.co/playground/code/riyh6z14zxio


def helper(i, cost, n, memo):
    if i in memo:
        return memo[i]
    
    if i >= n:
        return 0
    if i == n - 1:
        return cost[i]
    
    take_one_step = helper(i + 1, cost, n, memo)
    take_two_steps = helper(i + 2, cost, n, memo)
    
    memo[i] = cost[i] + min(take_one_step, take_two_steps)
    return memo[i]

def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    memo = {}
    return min(helper(0, cost, n, memo), helper(1, cost, n, memo))

