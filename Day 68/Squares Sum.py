https://my.newtonschool.co/playground/code/hxsngqzv4h00


N = int(input())
assert 1 <= N <= 10**5
sum_ = 0
for i in range(1, N + 1):
    sum_ += i * i
print(sum_)
