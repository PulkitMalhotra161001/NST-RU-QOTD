https://my.newtonschool.co/playground/code/vxw6xh6khyo1


def generate_binary_strings(n, current_string=""):
    if len(current_string) == n:
        print(current_string)
        return
    
    generate_binary_strings(n, current_string + "0")
    generate_binary_strings(n, current_string + "1")


# Driver Code 
if __name__ == "__main__": 
    n = int(input())
    assert 1 <= n <= 15
    generate_binary_strings(n)
