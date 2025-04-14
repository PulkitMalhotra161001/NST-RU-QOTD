https://my.newtonschool.co/playground/code/w0b42xgq9dir


def solve(k, s):
    if len(s[0]) >= k:
        return
    t = ""
    for char in s[0]:
        t += chr(ord(char) + 1)
    s[0] += t
    solve(k, s)

def kthCharacter(k):
    s = ["a"]  # Using a list to pass by reference
    solve(k, s)
    return s[0][k - 1]
