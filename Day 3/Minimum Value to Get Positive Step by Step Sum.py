https://my.newtonschool.co/playground/code/olou2mpznwqb


def minStartValue(nums):
    ans = 0
    sum_so_far = 0
    for el in nums:
        sum_so_far += el
        ans = min(ans, sum_so_far)
    return -ans + 1
