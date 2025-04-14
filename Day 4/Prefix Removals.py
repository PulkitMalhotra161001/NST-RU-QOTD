https://my.newtonschool.co/playground/code/3l4plpxxp2mv


t = int(input())
for _ in range(t):
    s = list(input())
    v = [0] * 256
    for char in s:
        v[ord(char) - ord('a')] += 1
    ans = []
    for i in range(len(s)):
        v[ord(s[i]) - ord('a')] -= 1
        if v[ord(s[i]) - ord('a')] == 0:
            ans = s[i:]
            break
    print(''.join(ans))
