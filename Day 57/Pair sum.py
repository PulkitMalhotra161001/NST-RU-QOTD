https://my.newtonschool.co/playground/code/7zjk6gtoc345


def pairSum(head, x):
    start=head
    end=head
    ans=0
    while end.next :
        end=end.next
    
    while start.data<end.data:
        s=start.data+end.data
        if s==x:
            ans+=1
            start=start.next
            end=end.prev
        elif s>x:
            end=end.prev
        else: 
            start=start.next
    return ans
