https://my.newtonschool.co/playground/code/5w9zjuh0wyhp


def merge(intervals):
    ans = []
    
    if not intervals:
        return ans
    
    intervals.sort()
    ans.append(intervals[0])
    j = 0
    
    for i in range(1, len(intervals)):
        if ans[j][1] >= intervals[i][0]:
            ans[j][1] = max(ans[j][1], intervals[i][1])
        else:
            j += 1
            ans.append(intervals[i])
    
    return ans
