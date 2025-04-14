https://my.newtonschool.co/playground/code/wcv0q51omeay


def answerQueries(nums, queries):
    n = len(nums)
    m = len(queries)
    nums.sort()

    # Create prefix sum array
    p = [0] * n
    total = 0
    for i in range(n):
        total += nums[i]
        p[i] = total

    # Process each query
    for i in range(m):
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if p[mid] <= queries[i]:
                low = mid + 1
            else:
                high = mid - 1

        queries[i] = high + 1

    return queries
