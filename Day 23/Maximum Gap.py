https://my.newtonschool.co/playground/code/4zsngrsx3jbp


import math
import sys

def maximum_gap(nums):
    n = len(nums)
    if n < 2:
        return 0

    minn = min(nums)
    maxx = max(nums)

    gap = math.ceil((maxx - minn) / (n - 1)) if n > 1 else 1
    if gap < 1:
        gap = 1

    arr = [[sys.maxsize, -sys.maxsize] for _ in range(n)]

    for i in nums:
        pos = (i - minn) // gap
        arr[pos][0] = min(arr[pos][0], i)
        arr[pos][1] = max(arr[pos][1], i)

    prev = minn
    res = 0
    for bucket in arr:
        if bucket[0] == sys.maxsize:
            continue
        res = max(res, bucket[0] - prev)
        prev = bucket[1]

    return res

# Input reading
if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))
    print(maximum_gap(v))
