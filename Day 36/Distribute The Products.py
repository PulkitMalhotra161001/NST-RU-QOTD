https://my.newtonschool.co/playground/code/sgcabyoa9rw2


def solve(n, quantities, item):
    if item == 0:
        return False
    store = 0
    for product in quantities:
        store += (product - 1) // item + 1
        if store > n:
            return False
    return True

def minimizedMaximum(n, m, quantities):
    assert 1 <= m <= 10**5
    assert 1 <= n <= 10**5
    assert m <= n
    assert all(1 <= num <= 10**5 for num in quantities)
    low = 0
    high = max(quantities)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if solve(n, quantities, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
