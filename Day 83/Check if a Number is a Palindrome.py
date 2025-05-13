https://my.newtonschool.co/playground/code/4jswkiv8q04t


num = int(input())

original_num = num

reversed_num = 0

while num > 0:
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit  
    num //= 10  

if original_num == reversed_num:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
