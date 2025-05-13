https://my.newtonschool.co/playground/code/2r45kgyvxwzm


def max_spread(root: Node) -> int:
    if not root:
        return 0

    q = deque([(root, 0)])
    res = 0

    while q:
        n = len(q)
        minLevelId = q[0][1]
        left = right = 0

        for i in range(n):
            curr, idx = q.popleft()
            idx -= minLevelId  # Normalize index

            if curr.left:
                q.append((curr.left, idx * 2 + 1))
            if curr.right:
                q.append((curr.right, idx * 2 + 2))

            if i == 0:
                left = idx
            if i == n - 1:
                right = idx

        res = max(res, right - left + 1)

    return res
