https://my.newtonschool.co/playground/code/qtb56fq9f6c2


import sys
import math

INF = float('inf')

def coin_change(coins, amount):
    n = len(coins)
    dp = [[INF] * (amount + 1) for _ in range(n + 1)]

    # Base case: 0 amount requires 0 coins
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[i][j - coins[i - 1]] != INF:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

    return -1 if dp[n][amount] == INF else dp[n][amount]

def main():
    t = int(input())
    for _ in range(t):
        a = int(input())
        n = int(input())
        v = list(map(int, input().split()))
        result = coin_change(v, a)
        if result == -1:
            print("Not Possible")
        else:
            print(result)

if __name__ == "__main__":
    main()
