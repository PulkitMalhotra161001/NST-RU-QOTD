https://my.newtonschool.co/playground/code/lidp34p0vfd9


def invert_binary_tree(root):
    if not root:
        return None
    
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root
