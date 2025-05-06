https://my.newtonschool.co/playground/code/9z6v16mhpamy



def maxCrossingSum(arr, l, m, h):

	sm = 0
	left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + arr[i]

		if (sm > left_sum):
			left_sum = sm

	sm = 0
	right_sum = -1000
	for i in range(m, h + 1):
		sm = sm + arr[i]

		if (sm > right_sum):
			right_sum = sm
	return max(left_sum + right_sum - arr[m], left_sum, right_sum)

def maxSubArraySum(arr, l, h):
	if (l > h):
		return -10000
	if (l == h):
		return arr[l]
	m = (l + h) // 2
	return max(maxSubArraySum(arr, l, m-1),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))


N=int(input())
arr=list(map(int,input().split()))
n = len(arr)
if N==len(arr):
    max_sum = maxSubArraySum(arr, 0, n-1)
    print(max_sum)
