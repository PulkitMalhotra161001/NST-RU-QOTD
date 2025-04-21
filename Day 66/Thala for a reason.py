https://my.newtonschool.co/playground/code/84jmb4dpgjcb


n=int(input())
assert 1 <= n <= 100000, "n is out of bounds"

a = list(map(int, input().split()))
assert len(a) == n, "Array length does not match n"

assert all(-10**9 <= ai <= 10**9 for ai in a), "Array element out of bounds"

cnt=0

for i in range(0,n):
    cnt+=(a[i]%7==0)

print(cnt)
