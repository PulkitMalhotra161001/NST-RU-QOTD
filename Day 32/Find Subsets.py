https://my.newtonschool.co/playground/code/hksvkoq4t2w6


def findSubsets(nums):
    res = []
    n = len(nums)
    for i in range(1 << n):  # 2^n subsets
        cur = []
        for j in range(n):
            if i & (1 << j):
                cur.append(nums[j])
        res.append(cur)
    return res
