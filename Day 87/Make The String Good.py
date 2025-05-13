https://my.newtonschool.co/playground/code/a0r2oz4e8zyf


def make_good(str):
    stack = []
    for char in str:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
