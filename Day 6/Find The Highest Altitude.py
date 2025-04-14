https://my.newtonschool.co/playground/code/qlug2paovabd


def largestAltitude(gain):
    maxAltitude = 0
    currentAltitude = 0
    
    for value in gain:
        currentAltitude += value
        maxAltitude = max(maxAltitude, currentAltitude)
    
    return maxAltitude
