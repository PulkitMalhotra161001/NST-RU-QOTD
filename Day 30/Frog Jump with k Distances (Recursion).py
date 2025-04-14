https://my.newtonschool.co/playground/code/t9ou4xt5ut0x


def frogJump(N,heights, K):
    def frog_jump(n, k, heights):
        if n == 0:
            return 0  # Base case: no energy needed at the start

        min_energy = float('inf')
        for jump in range(1, k + 1):
            if n - jump >= 0:  # Ensure the jump is within bounds
                cost = abs(heights[n] - heights[n - jump]) + frog_jump(n - jump, k, heights)
                min_energy = min(min_energy, cost)
        return min_energy
    return (frog_jump(N-1, K, heights))

# Example of custom input handling:
