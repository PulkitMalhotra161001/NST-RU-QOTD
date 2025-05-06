https://my.newtonschool.co/playground/code/8j8vob33htbb


def check(root, value):
    if not root:
        return True
    return root.val == value and check(root.left, value) and check(root.right, value)

def is_unival_tree(root):
    return check(root, root.val)
