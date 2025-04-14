https://my.newtonschool.co/playground/code/e3uempxi7slt


def runningSum(nums):
    n = len(nums)
    total = 0
    ans = [0] * n
    for i in range(n):
        total += nums[i]
        ans[i] = total
    return ans

