https://my.newtonschool.co/playground/code/375mes6ltws5


n = int(input())
lst = list(map(int,input().split()))
Q = int(input())
while Q:
    ans=0
    l,r = map(int,input().split())
    for i in range(l,r+1):
        ans += (1 if lst[i]%5 == 0 else 0)
    print(ans)
    Q -= 1
