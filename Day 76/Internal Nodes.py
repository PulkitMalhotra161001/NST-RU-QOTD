https://my.newtonschool.co/playground/code/glx1bfn39r4z


def internal_nodes(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 0
    
    return 1 + internal_nodes(root.left) + internal_nodes(root.right)
