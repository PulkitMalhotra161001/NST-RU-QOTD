https://my.newtonschool.co/playground/code/muswyan1rfbg


def col_sum(mat):
    col = -1
    maxEle = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > maxEle:
                maxEle = mat[i][j]
                col = j
    colSum = 0
    for i in range(len(mat)):
        colSum += mat[i][col]
    return colSum
