https://my.newtonschool.co/playground/code/o5h2iacin6wa


def numberOfTripsForGivenTime(a, givenTime):
    totalTrips = 0
    for x in a:
        val = x  # convert it to long long int is implicit in Python
        totalTrips += (givenTime // val)
    return totalTrips

def min_time(times, totalTrips):
    lowestTime = 1
    highestTime = int(1e14)
    while lowestTime < highestTime:
        mid = lowestTime + (highestTime - lowestTime) // 2

        if numberOfTripsForGivenTime(times, mid) >= totalTrips:
            highestTime = mid
        else:
            lowestTime = mid + 1
    return lowestTime
