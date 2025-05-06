https://my.newtonschool.co/playground/code/145nizuiok6q


def maxProfit(prices):
    if not prices:
        return 0
    
    A = -prices[0]
    B = float('-inf')
    C = float('-inf')
    D = float('-inf')
    
    for price in prices:
        A = max(A, -price)
        B = max(B, A + price)
        C = max(C, B - price)
        D = max(D, C + price)
        
    return D
