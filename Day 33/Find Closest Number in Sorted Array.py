https://my.newtonschool.co/playground/code/ivunp20b4oqe


def findClosest(arr, k):
    n = len(arr)
    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] <= k:
            i = mid + 1
        else:
            j = mid - 1
    
    a, b = float('inf'), float('inf')
    if j >= 0:
        a = abs(arr[j] - k)
    if i < n:
        b = abs(arr[i] - k)
    
    if b <= a:
        return arr[i]
    else:
        return arr[j]
