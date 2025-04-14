https://my.newtonschool.co/playground/code/n2kdkanwyfc6


def searchRange(nums, target):
    ans = []
    index1, index2 = -1, -1
    n = len(nums)
    start, end = 0, n - 1

    # Finding first occurrence
    while start <= end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            index1 = mid
            end = mid - 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    start, end = 0, n - 1

    # Finding last occurrence
    while start <= end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            index2 = mid
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    ans.append(index1)
    ans.append(index2)
    return ans

