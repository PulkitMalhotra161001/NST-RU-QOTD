https://my.newtonschool.co/playground/code/1tyrpe6cdinv


n = int(input())
arr = list(map(int,input().split()))

arr.sort()
tgt = arr[n//2]
ans=0
for i in arr:
    ans+=abs(i-tgt)
print(ans)
