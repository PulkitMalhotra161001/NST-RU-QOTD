https://my.newtonschool.co/playground/code/kazxioxd7r7b


def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
