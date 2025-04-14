https://my.newtonschool.co/playground/code/g0l34p0cooi9


from collections import deque
def findTheWinner(n, k):
    q = deque([x + 1 for x in range(n)])
    while len(q) > 1:
        c = k - 1
        while c:
            q.append(q.popleft())
            c -= 1        
        q.popleft()
    return q[0]
