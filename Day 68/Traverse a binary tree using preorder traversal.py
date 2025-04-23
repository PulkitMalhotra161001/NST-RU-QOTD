https://my.newtonschool.co/playground/code/tr5u8k68q9qp


def preorder(root, result):
    if not root:
        return
    
    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)

def preorder_traversal(root):
    if not root:
        return []
    result = []
    preorder(root, result)
    return result
