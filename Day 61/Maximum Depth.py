https://my.newtonschool.co/playground/code/vqiur5ud5n4p


# Your code here
def depth_of_string_stack(s):
    stack = []
    max_depth = 0
    for char in s:
        if char == '(':
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char == ')':
            stack.pop()
    return max_depth


