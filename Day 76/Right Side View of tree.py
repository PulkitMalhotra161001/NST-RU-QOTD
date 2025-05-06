https://my.newtonschool.co/playground/code/56r84uniz2l7


def right_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()
            
            # If it's the last  node of this level, add it to the result
            if i == level_size - 1:
                result.append(current.val)
            
            # Add left child to queue
            if current.left:
                queue.append(current.left)
            
            # Add right child to queue
            if current.right:
                queue.append(current.right)

    return result
