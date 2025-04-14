https://my.newtonschool.co/playground/code/sas2hxfumvf3


def maxSum(n, arr):
    if n == 1:
        print(arr[0])
        return 0

    inc = arr[1]
    exc = arr[0]

    for i in range(2, n):
        newInc = arr[i] + exc
        newExc = max(inc, exc)

        inc = newInc
        exc = newExc

    return max(inc, exc)
