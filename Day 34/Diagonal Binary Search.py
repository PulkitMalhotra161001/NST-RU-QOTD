https://my.newtonschool.co/playground/code/pm1ja2nm074i


def searchMatrix(matrix, target):
    n = len(matrix)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[mid][mid] == target:
            return True
        elif matrix[mid][mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
target = int(input())
print(searchMatrix(matrix,target))
