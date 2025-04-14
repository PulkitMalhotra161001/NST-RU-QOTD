https://my.newtonschool.co/playground/code/nkkwnzki1gto


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Reading input
n = int(input())

# Calculating factorial and printing result
result = factorial(n)
print(result)
