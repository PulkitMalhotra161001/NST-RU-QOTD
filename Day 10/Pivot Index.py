https://my.newtonschool.co/playground/code/2hy1ierxos9u


def pivotIndex(nums):
    total = sum(nums)
    left_total = 0

    for i in range(len(nums)):
        right_total = total - left_total - nums[i]
        if right_total == left_total:
            return i
        left_total += nums[i]

    return -1
