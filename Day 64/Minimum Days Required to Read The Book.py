https://my.newtonschool.co/playground/code/t8axxi6xi0sc


def min_time(arr):
    N = len(arr)
    arr.sort()
    pre = [0] * (N + 1)
    pre[0] = arr[0]

    for i in range(1, N):
        pre[i] = arr[i] + pre[i - 1]

    ans = max(2 * arr[N - 1], pre[N - 1])
    return ans
