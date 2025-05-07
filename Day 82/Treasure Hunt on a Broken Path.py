https://my.newtonschool.co/playground/code/8ww1b6hw77h8


def max_treasure(caves, k):
    n = len(caves)
    dp = [0] * (n + 1)   
    for i in range(1, n + 1):
        skip = dp[i - 1]
        take = caves[i - 1]
        if i - k - 1 >= 0:
            take += dp[i - k - 1]
        dp[i] = max(skip, take)
    
    return dp[n]

n, k = map(int, input().split())
caves = list(map(int, input().split()))
result = max_treasure(caves, k)
print(result)
