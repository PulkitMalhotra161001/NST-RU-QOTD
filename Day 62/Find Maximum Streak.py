https://my.newtonschool.co/playground/code/uiu8eb0ld35w


def maxStreak(str, X):
    n = len(s)
    start = 0
    q = deque()
    ans = 0

    for i in range(n):
        if s[i] == '0':
            if len(q) == X:
                if X == 0:
                    start = i + 1
                else:
                    ind = q.popleft()
                    q.append(i)
                    start = ind + 1
            else:
                q.append(i)
        ans = max(ans, i - start + 1)
    
    return ans
