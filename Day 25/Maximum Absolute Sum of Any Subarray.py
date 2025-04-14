https://my.newtonschool.co/playground/code/l00oc68jeeg4


def maxAbsoluteSum(nums):
    sum, minSum, maxSum = 0, 0, 0
    for num in nums:
        sum += num
        maxSum = max(maxSum, sum)
        minSum = min(minSum, sum)
    return abs(maxSum - minSum)
