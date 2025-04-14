https://my.newtonschool.co/playground/code/p91qdoqwabq2


def arrangeCoins(n):
    count = 0
    sum_ = 0
    ans = 0
    
    for i in range(1, n + 1):
        sum_ += i
        n -= sum_
        if n >= 0:
            ans = i
        sum_ = 0
    
    return ans
