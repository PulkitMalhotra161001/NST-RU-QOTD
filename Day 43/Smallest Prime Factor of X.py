https://my.newtonschool.co/playground/code/tiu7cgzh5jed


MAXN = 1000000
spf = [1] * (MAXN + 1)

def sieve():
    global spf
    spf[0] = 0
    for i in range(2, MAXN + 1):
        if spf[i] == 1:
            for j in range(i, MAXN + 1, i):
                if spf[j] == 1:
                    spf[j] = i

sieve()

# Read input
n = int(input())

# Assertion to ensure N is within the valid range
assert 1 <= n <= 100000, "N must be in the range [1, 100000]"

v = list(map(int, input().split()))

# Assertion to ensure the length of v is exactly N
assert len(v) == n, "The length of v must be exactly N"

# Assertion to ensure each element in v is within the valid range
assert all(2 <= x <= 1000000 for x in v), "Each v[i] must be in the range [2, 1000000]"

for num in v:
    print(spf[num], end=" ")
