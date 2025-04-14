https://my.newtonschool.co/playground/code/fd6qt0qv7hf4


def solve(v):
    n = len(v)
    last = n - 1
    for i in range(n - 2, -1, -1):
        if i + v[i] >= last:
            last = i
    if last == 0:
        print("true")
    else:
        print("false")

n = int(input())
v = list(map(int, input().split()))
solve(v)
