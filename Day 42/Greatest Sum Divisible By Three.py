https://my.newtonschool.co/playground/code/s0gg2j1az5ar


def solve(i, nums, r):
    if i == len(nums):
        return 0 if r % 3 == 0 else -1000000
    
    op1 = nums[i] + solve(i + 1, nums, (r + nums[i]))
    op2 = solve(i + 1, nums, r)
    
    return max(op1, op2)

def maxSumDivThree(nums):
    return solve(0, nums, 0)
