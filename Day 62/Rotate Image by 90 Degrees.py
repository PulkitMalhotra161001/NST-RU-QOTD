https://my.newtonschool.co/playground/code/s19a8wl7qt4c


def modifyMat(a,n):
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    # Reverse the elements in each row
    for i in range(n):
        a[i] = a[i][::-1]
