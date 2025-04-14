https://my.newtonschool.co/playground/code/ljtx8f76x9hp


def frogJump(heights):
    n = len(heights)
    dp = [-1 for __ in range(n + 1)]
    dp[n] = 0
    dp[n - 1] = abs(heights[n - 2] - heights[n - 1])

    for i in range(n - 2, 0, -1):

        oneJump = dp[i + 1] + abs(heights[i - 1] - heights[i])
        twoJump = dp[i + 2] + abs(heights[i - 1] - heights[i + 1])

        dp[i] = min(oneJump, twoJump)

    ans = dp[1]
    return ans
