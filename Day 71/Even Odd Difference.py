https://my.newtonschool.co/playground/code/asb4fjqi70hg


def even_odd_diff(arr):
    ans = 0
    for i in range(len(arr)):
        if i % 2:
            ans -= arr[i]
        else:
            ans += arr[i]
    return ans
