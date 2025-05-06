https://my.newtonschool.co/playground/code/01ogkaflr7n9


def parent(root, X, prev):
    if not root:
        return -1
    if root.val == X:
        return prev
    left = parent(root.left, X, root.val)
    right = parent(root.right, X, root.val)
    return left if left != -1 else right

def parent_node(root, X):
    return parent(root, X, -1)
