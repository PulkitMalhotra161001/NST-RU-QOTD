https://my.newtonschool.co/playground/code/awyxo78v8jiv


def count(nums, bound):
    ans = 0
    cnt = 0
    for x in nums:
        cnt = cnt + 1 if x <= bound else 0
        ans += cnt
    return ans

def numSubarrayBoundedMax(nums, left, right):
    return count(nums, right) - count(nums, left - 1)

