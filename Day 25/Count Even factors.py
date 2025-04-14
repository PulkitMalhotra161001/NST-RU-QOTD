https://my.newtonschool.co/playground/code/unbg033askc0


n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0 and i%2==0):
        count+=1
print(count)
