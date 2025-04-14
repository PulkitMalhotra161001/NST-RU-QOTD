https://my.newtonschool.co/playground/code/rj5tu9i5zykn


lst = list(map(int,input().split()))
q = int(input())
n = len(lst)
prefix_sum = [0] * (n + 1)
    
    
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + lst[i - 1]


while q:
    L,R = map(int,input().split())
    print(prefix_sum[R + 1] - prefix_sum[L])
    q = q-1

