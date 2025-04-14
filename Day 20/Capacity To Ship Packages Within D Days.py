https://my.newtonschool.co/playground/code/lzih418y558q


def shipWithinDays(weights, D):
    max_weight = max(weights)
    total_weight = sum(weights)
    left = max_weight
    right = total_weight

    while left < right:
        mid = (left + right) // 2
        days_needed = 1
        curr_weight = 0

        for weight in weights:
            if curr_weight + weight > mid:
                days_needed += 1
                curr_weight = 0
            curr_weight += weight

        if days_needed > D:
            left = mid + 1
        else:
            right = mid

    return left
