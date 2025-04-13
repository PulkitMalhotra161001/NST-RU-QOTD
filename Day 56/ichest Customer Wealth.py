https://my.newtonschool.co/playground/code/9cwwffxoeh6n


m , n = map(int,input().split())
assert 1 <= m <= 100
assert 1 <= n <= 100
maxi = 0
for i in range(m):
    li = list(map(int,input().split()))
    for num in li:
        assert(num >= 1 and num <= 100000)
    maxi = max(maxi, sum(li))
print(maxi)
