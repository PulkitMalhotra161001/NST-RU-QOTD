https://my.newtonschool.co/playground/code/ucdglh7hfajo


def parity_queries(arr, queries):
    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            total += arr[i]
        else:
            total -= arr[i]
        arr[i] = total
    results = []
    for i in queries:
        l, r = i
        if l == 0:
            results.append(arr[r])
        else:
            results.append(arr[r] - arr[l - 1])
    return results
