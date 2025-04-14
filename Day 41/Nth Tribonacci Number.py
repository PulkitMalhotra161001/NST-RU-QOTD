https://my.newtonschool.co/playground/code/2u2l3cnwmsjf


def tribonacci(n):
    # Base cases
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    
    # Recursive case
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

N = int(input())
print(tribonacci(N))
