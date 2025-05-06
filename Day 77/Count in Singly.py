https://my.newtonschool.co/playground/code/8aajmi8ed3v4


def count_occurrences(head, K):
  cnt = 0
  temp = head
  
  while temp:
    if temp.data==K:
      cnt+=1
    
    temp=temp.next
    
  return cnt
