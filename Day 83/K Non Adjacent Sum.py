https://my.newtonschool.co/playground/code/1t1cea2y1md4


def max_sum(arr, K):
    memo = {}
    def solve(ind, K, prev, arr):
        if (ind, K, prev) in memo:
            return memo[(ind, K, prev)]
        
        if ind == len(arr) or K == 0:
            return 0
        
        ans = solve(ind + 1, K, 0, arr)

        if prev == 0:
            ans = max(ans, arr[ind] + solve(ind + 1, K - 1, 1, arr))

        memo[(ind, K, prev)] = ans
        return ans

    return solve(0, K, 0, arr)
