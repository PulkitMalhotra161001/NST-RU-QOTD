https://my.newtonschool.co/playground/code/xpolvtb65a6d


def searchMatrix(mat, target):
      #write your code here
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
