https://my.newtonschool.co/playground/code/hn5tpoerwsvb


def findFrequency(left, right, element, store):
    if element not in store:
        return 0
    a = bisect.bisect_left(store[element], left)
    b = bisect.bisect_right(store[element], right)
    return b - a

def numOfFreq(arr, queries):
    store = {}
    n = len(arr)
    for i in range(n):
        if arr[i] not in store:
            store[arr[i]] = []
        store[arr[i]].append(i)
    ans = []
    for it in queries:
        x = it[0]
        y = it[1]
        wt = it[2]
        as_ = findFrequency(x, y, wt, store)
        ans.append(as_)
    return ans
