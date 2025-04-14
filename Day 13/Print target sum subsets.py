https://my.newtonschool.co/playground/code/hk736di5vm58


def find_subsets(nums, target):
        def subset(nums, curr, target, result):
            if not nums:
                if sum(curr) == target:
                    result.append(curr)
                return

            # Include the current number
            subset(nums[1:], curr + [nums[0]], target, result)
            # Exclude the current number
            subset(nums[1:], curr, target, result)

        result = []
        subset(nums, [], target, result)
        return result
