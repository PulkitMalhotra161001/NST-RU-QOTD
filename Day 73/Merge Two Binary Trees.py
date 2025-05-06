https://my.newtonschool.co/playground/code/fwr9amegqbbl


def merge_trees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    root = Node(root1.val + root2.val)
    root.left = merge_trees(root1.left, root2.left)
    root.right = merge_trees(root1.right, root2.right)
    return root
