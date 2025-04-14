https://my.newtonschool.co/playground/code/jmpc964yquko


t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    i, j = 0, n - 1
    while i <= j:
        print(v[i], end=" ")
        i += 1
        if i <= j:
            print(v[j], end=" ")
            j -= 1
    print()
