https://my.newtonschool.co/playground/code/frx1r70941j3


def maxAmount(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h_left = height[left]
        h_right = height[right]
        width = right - left
        min_height = min(h_left, h_right)

        max_area = max(max_area, width * min_height)

        if h_left < h_right:
            left += 1
        else:
            right -= 1

    return max_area
