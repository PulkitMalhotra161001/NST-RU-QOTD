https://my.newtonschool.co/playground/code/fc30vh02bgxn


def rightSideView(root):
    ans = []
    if not root:
        return ans
    
    q = deque([root])
    
    while q:
        size = len(q)
        data = []
        
        for _ in range(size):
            temp = q.popleft()
            data.append(temp.val)
            
            if temp.left:
                q.append(temp.left)
                
            if temp.right:
                q.append(temp.right)
        
        ans.append(data[-1])
    
    return ans
