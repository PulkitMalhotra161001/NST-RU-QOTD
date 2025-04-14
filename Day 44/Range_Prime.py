https://my.newtonschool.co/playground/code/unqgwroo4na5


# Your code here
N = 1000001
prime = [0] * N

for i in range(2, int(N ** 0.5) + 1):
    if prime[i] == 0:
        for j in range(i * i, N, i):
            prime[j] = 1;

prime[0] = 1
prime[1] = 1

ans = 0
l, r = map(int, input().split())
assert l <= r
assert 1 <= l <= 1000000
assert 1 <= r <= 1000000
for i in range(l, r + 1):
    if prime[i] == 0:
        ans += 1

print(ans)
