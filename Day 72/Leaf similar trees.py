https://my.newtonschool.co/playground/code/t6lgdpfvoxow


def is_leaf_similar(root1, root2):
    def get_leaf_sequence(root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return get_leaf_sequence(root.left) + get_leaf_sequence(root.right)
    
    leaves1 = get_leaf_sequence(root1)
    leaves2 = get_leaf_sequence(root2)
    if leaves1 == leaves2:
        return 1
    return 0
