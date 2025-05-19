https://my.newtonschool.co/playground/code/k5x9jc2hinw8


def max(a, b):
    return a if a > b else b

def knapSackHelper(W, w, v, n, dp):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if w[n - 1] > W:
        dp[n][W] = knapSackHelper(W, w, v, n - 1, dp)
    else:
        dp[n][W] = max(v[n - 1] + knapSackHelper(W - w[n - 1], w, v, n - 1, dp), 
                       knapSackHelper(W, w, v, n - 1, dp))

    return dp[n][W]

def maxWeight(w, v, W):
    N = len(w)
    dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]
    return knapSackHelper(W, w, v, N, dp)
