https://my.newtonschool.co/playground/code/72qh3o9clrud


n=int(input())
assert 1 <= n <= 100, "n is out of bounds"

arr = list(map(int, input().split()))
assert len(arr) == n, "Array length does not match n"

for val in arr:
  assert 1 <= val <= 100

k, l, r = map(int,input().split())

assert 1 <= k <= 100
assert 1 <= l <= 100
assert 1 <= r <= 100

ans=0

for val in arr:
  if val%k==0 and l<= val <=r:
    ans+=val

print(ans)
