https://my.newtonschool.co/playground/code/mjvm6h0y0kzi


def maxSum(l,k):
    curr_sum=0
    for x in range(k):
        curr_sum=curr_sum+l[x]
    max_sum=curr_sum
    i=0
    j=k
    while i<len(l)-k:
        curr_sum=curr_sum-l[i]+l[j]
        max_sum=max(max_sum,curr_sum)
        i+=1
        j+=1
    return max_sum

N, K = map(int,input().split(' '))
assert 1 <= K <= N <= 200000
A = list(map(int, input().split(' ')))
assert -200000 <= min(A) and max(A) <= 200000
print(maxSum(A,K))
