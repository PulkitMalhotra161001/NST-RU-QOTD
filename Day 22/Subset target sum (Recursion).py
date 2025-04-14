https://my.newtonschool.co/playground/code/1af3d5xzuzvd


def count_subsets(nums, n, k):
    if n == 0:
        return k == 0  # No subsets possible if array is empty
    if k == 0:
        return 1  # Empty subset always has sum 0

    include = count_subsets(nums, n - 1, k - nums[n - 1])
    exclude = count_subsets(nums, n - 1, k)

    return include + exclude
if __name__ == "__main__":
    # Input
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    cnt = count_subsets(nums,n,k)
    if(cnt):
        print("true")
    else:
        print("false")
