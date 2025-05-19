https://my.newtonschool.co/playground/code/k7igmjoh8i4x


def min_diff(root):
    prev = None
    ans = float('inf')

    def dfs(node):
        nonlocal prev, ans  # Ensure prev and ans refer to the outer scope variables
        if node:
            dfs(node.left)
            if prev is not None:
                ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)

    dfs(root)
    return ans
