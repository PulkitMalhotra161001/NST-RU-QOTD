https://my.newtonschool.co/playground/code/oc5mpkydj2nd


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
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    # count = 0
    # for j in range(1<<n):
    #     s = 0
    #     for i in range(n):
    #         if(j&(1<<i)):
    #             s += nums[i]
    #     if(s == k):
    #         count+=1
    print(count_subsets(nums,n,k))
