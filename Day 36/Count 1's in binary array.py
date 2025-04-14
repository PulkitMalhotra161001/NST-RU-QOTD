https://my.newtonschool.co/playground/code/psqwlilii3pg


def count_ones(arr, n):
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == 1:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    # Output the count of 1's
    print(count_ones(array, n))
