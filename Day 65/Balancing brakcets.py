https://my.newtonschool.co/playground/code/esw0032vzk1n


def is_balanced_brackets(s):
    stack = []
    
    for ch in s:
        if ch in (')', '}', ']'):
            if not stack:
                print("NO")
                return

            if (ch == ')' and stack[-1] == '(') or \
               (ch == '}' and stack[-1] == '{') or \
               (ch == ']' and stack[-1] == '['):
                stack.pop()
            else:
                print("NO")
                return
        else:
            stack.append(ch)

    print("YES" if not stack else "NO")


t = int(input().strip())  
assert(1 <= t <= 100)
for _ in range(t):
    s = input().strip()
    n=len(s)
    assert(1 <= n <= 100)
    for x in s:
      assert(x=='(' or  x=='{' or x=='[' or  x==']' or x=='}' or  x==')')
    is_balanced_brackets(s)
