https://my.newtonschool.co/playground/code/ryfs65yrqw9c


def findPeakElement(nums):
    n = len(nums)
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low
