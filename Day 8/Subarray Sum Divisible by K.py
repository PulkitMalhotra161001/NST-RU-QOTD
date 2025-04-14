https://my.newtonschool.co/playground/code/ysb6g6gzd68a


def sub_count(arr, k):
    # Create a list to store frequency of mod values
    mod = [0] * k

    cum_sum = 0
    for num in arr:
        cum_sum += num
        # Handle negative numbers
        mod[((cum_sum % k) + k) % k] += 1

    result = 0
    for count in mod:
        if count > 1:
            result += (count * (count - 1)) // 2

    # Include subarrays which themselves are divisible by k
    result += mod[0]

    return result


# Driver code
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sub_count(arr, k))
