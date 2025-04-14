https://my.newtonschool.co/playground/code/rihtyegfntew


def solve(v, ind):
    if len(v) <= ind:
        return 0
    else:
        return max(v[ind] + solve(v, ind + 2), solve(v, ind + 1))

n = int(input())
v = list(map(int, input().split()))
a, b = [], []

for i in range(n):
    if i != 0:
        a.append(v[i])
    if i != n - 1:
        b.append(v[i])

print(max(solve(a, 0), solve(b, 0)))
