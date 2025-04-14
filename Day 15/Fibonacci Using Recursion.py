https://my.newtonschool.co/playground/code/jfwo7hjy9auq


# Your code here
n = int(input())

a= 0
b=1
c=1
for i in range(n-1):
    c= a+b
    a=b
    b=c 

print(c)
