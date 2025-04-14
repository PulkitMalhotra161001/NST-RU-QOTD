https://my.newtonschool.co/playground/code/gjbmr5dljc1s


def subarray_exists(arr, n):
    s = set()
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == 0 or prefix_sum in s:
            return True

        s.add(prefix_sum)

    return False
