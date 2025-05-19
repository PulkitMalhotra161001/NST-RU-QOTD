https://my.newtonschool.co/playground/code/wwrc2b1dno02


# Your code here
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 0:
        print(a[i], end = " ")
