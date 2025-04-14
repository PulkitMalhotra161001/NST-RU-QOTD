https://my.newtonschool.co/playground/code/sh4ac3agkf4e


def solve(k):
    low, high = 0, k

    while low <= high:
        mid = low + (high - low) // 2
        equation_value = 2 * mid * mid + 5 * mid

        if equation_value == k:
            return mid
        elif equation_value < k:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    k = int(input())

    result = solve(k)

    if result != -1 and result != 0:
        print(result)
    else:
        print("-1")
