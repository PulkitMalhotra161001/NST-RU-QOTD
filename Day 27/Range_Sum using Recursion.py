https://my.newtonschool.co/playground/code/dzj0ca2xi8z7


def rangeSum(L, R):
    if L > R:
        return 0
    return L + rangeSum(L + 1, R)


