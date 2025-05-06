https://my.newtonschool.co/playground/code/8vx8y96ivh8a


def pos_node_sum(root):
    if root is None:
        return 0
    
    left_sum = pos_node_sum(root.left)
    right_sum = pos_node_sum(root.right)
    
    return (root.val if root.val > 0 else 0) + left_sum + right_sum
