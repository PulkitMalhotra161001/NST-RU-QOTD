https://my.newtonschool.co/playground/code/e0000lb0k2vg


def subarraySumLL(head, k):
    #Write your code here
    res=0
    curSum=0
    prefixSums={0:1}
    cur = head
    while(cur != None):
        curSum+= cur.data
        diff=curSum-k
        res+=prefixSums.get(diff,0)
        prefixSums[curSum]=1+prefixSums.get(curSum,0)
        cur = cur.next
    return res
