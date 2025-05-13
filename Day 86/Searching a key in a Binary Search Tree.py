https://my.newtonschool.co/playground/code/1siol2wij6m8


def search_in_bst(root, key):
    if not root:
        return 0
    if root.val == key:
        return 1
    if key < root.val:
        return search_in_bst(root.left, key)
    return search_in_bst(root.right, key)
