https://my.newtonschool.co/playground/code/f9pi7eoou615


def isPresent(arr, x):
    assert 1 <= len(arr) <= 10**6, "Array length must be in the range [1, 10^6]"
    assert 1 <= x <= 10**9, "Search element X must be in the range [1, 10^9]"
    assert 1 <= arr[0]
    assert arr[-1] <= 10**9

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False
