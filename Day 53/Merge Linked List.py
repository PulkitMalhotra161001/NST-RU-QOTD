https://my.newtonschool.co/playground/code/3nape7wtm3kl


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    prev = None
    temp = head1
    while(temp):
        prev = temp
        temp = temp.next
    prev.next = head2
    return head1
    
