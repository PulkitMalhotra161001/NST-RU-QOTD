https://my.newtonschool.co/playground/code/eoy27w7fie8n


def solve_util(n, height, dp, k):
    dp[0] = 0

    for i in range(1, n):
        min_steps = float('inf')

        for j in range(1, k + 1):
            if i - j >= 0:
                jump = dp[i - j] + abs(height[i] - height[i - j])
                min_steps = min(jump, min_steps)

        dp[i] = min_steps

    return dp[n - 1]

def frogJump(n, height, k):
    dp = [-1] * n
    return solve_util(n, height, dp, k)
