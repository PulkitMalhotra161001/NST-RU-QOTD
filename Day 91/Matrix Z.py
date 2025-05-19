https://my.newtonschool.co/playground/code/dcwxjefgf0xq


N = int(input())
assert 1 <= N <= 1000
lis = []
for _ in range(N):
    l = list(map(int, input().split(" ")))
    assert N == len(l)
    lis.append(l)
ans = 0 
for i in range(N):
    for j in range(N):
        if i == 0 or i == N-1:
            ans += lis[i][j]
        elif i+j == N-1:
            ans += lis[i][j]
print(ans)
