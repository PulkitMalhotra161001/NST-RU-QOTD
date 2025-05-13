https://my.newtonschool.co/playground/code/f6phqt20hiq5


def way(arr, i, dp):
    if i == len(arr) - 1:
        return 1
    if dp[i] != -1:
        return dp[i]
    dp[i] = 0
    for j in range(i + 1, len(arr)):
        if i + arr[i] >= j:
            dp[i] += way(arr, j, dp)
    return dp[i]

def count_ways(arr):
    n = len(arr)
    dp = [-1] * n
    return way(arr, 0, dp) 
