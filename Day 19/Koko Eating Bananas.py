https://my.newtonschool.co/playground/code/5opl6qxxdgwy


def blackbox(maxpiles, piles, h):
    hours = 0
    for i in piles:
        time = i // maxpiles
        hours += time
        if i % maxpiles != 0:
            hours += 1
    return hours <= h

def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)  # Simplified way to get the highest value in piles
    while low < high:
        mid = low + (high - low) // 2
        if blackbox(mid, piles, h):
            high = mid
        else:
            low = mid + 1
    return low



