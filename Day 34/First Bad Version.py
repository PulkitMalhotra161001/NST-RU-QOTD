https://my.newtonschool.co/playground/code/6qjihsabnj2r


def firstBadVersion(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low
