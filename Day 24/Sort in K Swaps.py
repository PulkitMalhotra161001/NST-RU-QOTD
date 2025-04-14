https://my.newtonschool.co/playground/code/9c6taq020msr


def bubbleSort(nums, k):
    n = len(nums)
    assert 1 <= n <= 3*(10**3)
    assert 1<=min(nums)<=max(nums)<=10**5
    assert 0<=k<=10**8
    count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                count += 1
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return count <= k
