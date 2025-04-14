https://my.newtonschool.co/playground/code/j5p88e17jao8


def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    # Three possible cases: 
    # 1. Product of the three largest positive numbers.
    # 2. If there are negative numbers, product of the two smallest negative numbers and the largest positive number.
    # 3. If there are no positive numbers, product of the three largest negative numbers.
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
