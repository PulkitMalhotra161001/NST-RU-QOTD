https://my.newtonschool.co/playground/code/atjdd9b77yj3


def canFindSum(nums, target, ind, n, d):
    if target in d: return d[target] 
    if target == 0: d[target] = True
    else:
        d[target] = False
        if target > 0:
            for i in range(ind, n):
                if canFindSum(nums, target - nums[i], i+1, n, d):
                    d[target] = True
                    break
    return d[target]

def canPartition(nums):
    s = sum(nums)
    if s % 2 != 0: return False
    return canFindSum(nums, s/2, 0, len(nums), {})
    

    
    
