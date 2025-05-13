https://my.newtonschool.co/playground/code/gyxvysppwaex


def sum_even_nodes(root):
    if not root:
        return 0
    sum=0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val % 2 == 0:
            sum += node.val
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return sum
