https://my.newtonschool.co/playground/code/mwizeetzoay2


def numSquares(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        min_val = float('inf')
        j = 1
        while j * j <= i:
            min_val = min(min_val, dp[i - j * j] + 1)
            j += 1
        dp[i] = min_val
    return dp[N]
