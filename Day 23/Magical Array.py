https://my.newtonschool.co/playground/code/nlotam0roiet


def magicalArrays(arr):
    n = len(arr)
    ans = 0
    i = 0
    
    while i < n:
        cnt = 1
        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1
            cnt += 1
        ans += (cnt * (cnt + 1)) // 2
        i += 1
    
    return ans
