https://my.newtonschool.co/playground/code/2gk2fzyvqa2y


def maximumUniqueSubarray(nums):
    seen = set()
    curr_sum, max_sum, l = 0, 0, 0
    for num in nums:
        while num in seen:
            curr_sum -= nums[l]
            seen.remove(nums[l])
            l += 1
        curr_sum += num
        seen.add(num)
        max_sum = max(max_sum, curr_sum)

    return max_sum
        


