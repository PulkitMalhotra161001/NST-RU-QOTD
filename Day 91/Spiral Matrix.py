https://my.newtonschool.co/playground/code/yl5nrazccpig


# Your code here
def spiral_matrix(matrix, n, m):
    top, bottom, left, right = 0, n - 1, 0, m - 1
    result = []

    while top <= bottom and left <= right:
        # Traverse top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Read input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = spiral_matrix(matrix, n, m)
print(*result)
