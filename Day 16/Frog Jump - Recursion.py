https://my.newtonschool.co/playground/code/hmr1e2v723g1


def frog_jump_helper(index, heights):
    # Base cases
    if index == 0:
        return 0
    if index == 1:
        return abs(heights[1] - heights[0])

    # Recursive step: Calculate the minimum cost to reach the current step
    one_step = frog_jump_helper(index - 1, heights) + abs(heights[index] - heights[index - 1])
    two_step = frog_jump_helper(index - 2, heights) + abs(heights[index] - heights[index - 2])
    
    return min(one_step, two_step)

def frogJump(heights):
    n = len(heights)
    return frog_jump_helper(n - 1, heights)
