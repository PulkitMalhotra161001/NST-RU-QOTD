https://my.newtonschool.co/playground/code/5pl9ijteohlx


def sumOddLengthSubarrays(arr):
    n = len(arr)
    answer = 0
    
    for i in range(n):
        left = i
        right = n - i - 1
        answer += arr[i] * (left // 2 + 1) * (right // 2 + 1)
        answer += arr[i] * ((left + 1) // 2) * ((right + 1) // 2)
    
    return answer
