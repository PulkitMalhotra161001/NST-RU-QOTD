https://my.newtonschool.co/playground/code/y1o042p60nxe


def even_sum(arr):
    ans = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            ans += arr[i]
    return ans
