https://my.newtonschool.co/playground/code/36rnd1cpu6uu


def count_subarrays(arr,K,a,b):
    ans = 0
    N = len(arr)

    for item in arr:
        assert 0 <= item <= 10**9
    count_as,count_bs = 0,0
    for i in range(K):
        count_as += (arr[i] == a)
        count_bs += (arr[i] == b)
    
    ans += (count_as == count_bs and count_as > 0 and count_bs > 0)
    for i in range(K,N):
        count_as += (arr[i]  == a)
        count_bs += (arr[i] == b)
        count_as -= (arr[i - K]  == a)
        count_bs -= (arr[i - K] == b)
        ans += (count_as == count_bs and count_as > 0 and count_bs > 0)

    return ans


N,K = map(int,input().split())
assert 1 <= N <= 10**5 and 1 <= K <= N
assert N >= K
arr = list(map(int,input().split()))
a,b = map(int,input().split())
print(count_subarrays(arr,K,a,b))
    
