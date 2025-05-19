https://my.newtonschool.co/playground/code/unuirjftvyt3


n = int(input())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
