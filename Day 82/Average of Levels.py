https://my.newtonschool.co/playground/code/3vjucl4oma03


def average_of_levels(root):
    ans = []
    if not root:
        return ans
    
    q = deque([root])
    
    while q:
        level_sum = 0
        level_count = len(q)
        
        for _ in range(level_count):
            node = q.popleft()
            level_sum += node.val
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        ans.append(level_sum / level_count)
    
    return ans
