https://my.newtonschool.co/playground/code/jl29f9f48nq8


def removeConsecutiveCharacter(S):
    stack = [""]
    for c in s:
      if stack[-1] == c:
        stack.pop()
      else:
        stack.append(c)
    return ''.join(stack)
