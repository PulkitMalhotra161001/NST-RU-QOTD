https://my.newtonschool.co/playground/code/yhkwyvc6zqj3


def min_speed(dist, hour):
    n = len(dist)  # Get the size of the input list 'dist' (number of distances to travel)
    minSpeed, maxSpeed = 1, 10**7 + 1  # Initialize the minimum and maximum possible speeds
    answer = -1  # Initialize the variable to store the final answer

    while minSpeed < maxSpeed:  # Binary search loop to find the minimum required speed
        midSpeed = minSpeed + (maxSpeed - minSpeed) // 2  # Calculate the middle speed

        totalHours = 0.0  # Initialize total travel time to 0

        # Calculate the total hours required to travel each distance at the current middle speed
        for i in range(n - 1):
            # Add the time taken to travel distance at index i using current midSpeed to totalHours
            totalHours += (dist[i] + midSpeed - 1) // midSpeed

        # Add the time taken to travel the last distance using current midSpeed to totalHours
        totalHours += dist[n - 1] / midSpeed

        if totalHours > hour:
            # If the total hours exceed the given hour, update minSpeed to consider higher speeds
            minSpeed = midSpeed + 1
        else:
            # If the total hours are within the given hour, update the answer to the current speed
            # and search for a potentially smaller speed in the lower half of the range.
            answer = midSpeed
            maxSpeed = midSpeed

    return answer
