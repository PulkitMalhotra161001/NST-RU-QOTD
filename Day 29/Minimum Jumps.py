https://my.newtonschool.co/playground/code/gdisrgqxd09e


import sys

def minSteps(v, ind):
    if ind >= len(v) - 1:
        return 0
    ans = sys.maxsize
    for i in range(1, v[ind] + 1):
        ans = min(ans, minSteps(v, ind + i))
    if ans == sys.maxsize:
        return sys.maxsize
    else:
        return ans + 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    ans = minSteps(v, 0)
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)

main()
