https://my.newtonschool.co/playground/code/vf4sso9oa4ev


import math

def repairCars(ranks, cars):
    left, right = 1, ranks[0] * cars * cars
    while left < right:
        mid = (left + right) // 2
        cur = 0
        for rank in ranks:
            cur += int(math.sqrt(mid / rank))
        if cur < cars:
            left = mid + 1
        else:
            right = mid
    return left


