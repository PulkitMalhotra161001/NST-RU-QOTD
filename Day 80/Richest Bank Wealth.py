https://my.newtonschool.co/playground/code/lzvx82r80nx4


def max_wealth(accounts):
  ans = 0
  n=len(accounts)
  m=len(accounts[0])
  
  for j in range(m):
    cur=0
    for i in range(n):
      cur+=accounts[i][j]
    ans=max(ans,cur)
  
  return ans
  
