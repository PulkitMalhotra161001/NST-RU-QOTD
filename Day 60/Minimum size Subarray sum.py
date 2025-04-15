https://my.newtonschool.co/playground/code/2f6im6w7475m


def min_subarray_len(target, arr):
    sum_ = 0
    left = 0
    min_length = float('inf')
    n = len(arr)

    for right in range(n):
        sum_ += arr[right]
        while sum_ >= target:
            min_length = min(min_length, right - left + 1)
            sum_ -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

target=int(input())
arr=list(map(int,input().split()))
print(min_subarray_len(target,arr))

