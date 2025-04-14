https://my.newtonschool.co/playground/code/z1cpb0fzkiu6


def is_power_of_four(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return n % 4 == 0 and is_power_of_four(n // 4)

n = int(input())
if is_power_of_four(n):
    print("True")
else:
    print("False")
