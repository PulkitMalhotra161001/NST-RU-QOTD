https://my.newtonschool.co/playground/code/yvmxdy6km7gy


n = int(input())
ans = 0
ispm = [0] * (n + 1)

for i in range(2, n + 1):
    if ispm[i] == 1:
        continue
    ans ^= i
    for j in range(2 * i, n + 1, i):
        ispm[j] = 1

print(ans)
