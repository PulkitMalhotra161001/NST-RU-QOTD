https://my.newtonschool.co/playground/code/h0m8gsozm7lu


def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False
