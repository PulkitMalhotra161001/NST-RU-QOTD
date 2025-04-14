https://my.newtonschool.co/playground/code/jvy2lmx0sovv


def maxScore(s):
    ones = s.count('1')
    
    ans = 0
    zeros = 0
    for i in range(len(s) - 1):
        if s[i] == '1':
            ones -= 1
        else:
            zeros += 1
        
        ans = max(ans, zeros + ones)
    
    return ans
