https://my.newtonschool.co/playground/code/7zlwk6nvokjd


def prime(n):
	for i in range(2,int(n**.5)+1):
		if(n%i==0):
			return False
	return True
def check(n):
	if(n%2==0):
		n +=1
	while(True):
		if(prime(n)==True):
			return n
		
		n +=2;
	return n
n=int(input())
x=check(n)
print(x-n)
