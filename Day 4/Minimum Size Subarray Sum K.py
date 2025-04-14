https://my.newtonschool.co/playground/code/qq3evisf7a6a


def minSubArray(arr, k):
    n = len(arr)
    mini = n+1
    j = 0
    cur = 0
    for i in range(n):
        while j < n and cur < k:
            cur+=arr[j]
            j+=1
        if cur >= k:
            mini=min(mini, j-i)
        cur-=arr[i]
    if mini > n: mini = 0
    return mini
