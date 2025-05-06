https://my.newtonschool.co/playground/code/seaoeb5evaly


def odd_sum(arr):
    ans = 0
    for i in range(len(arr)):
        if i % 2:
            ans += arr[i]
    return ans
