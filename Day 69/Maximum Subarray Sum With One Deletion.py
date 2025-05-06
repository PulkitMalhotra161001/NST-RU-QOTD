https://my.newtonschool.co/playground/code/u6oyiu5quz0x


def max_sum(arr):
    n = len(arr)
    ans = arr[0]
    noDel = arr[0]
    oneDel = 0

    for i in range(1, n):
        oneDel = max(oneDel + arr[i], noDel)
        noDel = max(noDel + arr[i], arr[i])
        ans = max(ans, oneDel, noDel)
    return ans
