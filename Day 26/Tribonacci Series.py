https://my.newtonschool.co/playground/code/g24teswq2xkh


def tri(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 1
    
    for i in range(3, n + 1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    
    return arr[n]
