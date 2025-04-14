https://my.newtonschool.co/playground/code/2rno6jh69lel


def solve(ind, n, k, s):
    if ind == n:
        return int(s[k - 1])
    
    cur = ""
    for i in s:
        if i == '0':
            cur += "01"
        else:
            cur += "10"
    
    return solve(ind + 1, n, k, cur)

def kthGrammar(n, k):
    return solve(1, n, k, "0")
