https://my.newtonschool.co/playground/code/p3qru5nwg3md


'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def intersection(head1,head2):
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    # Calculate lengths of both linked lists
    len1, len2 = getLength(head1), getLength(head2)
    
    # Adjust starting points for both lists to ensure they are equally far from the end
    while len1 > len2:
        head1 = head1.next
        len1 -= 1
    while len2 > len1:
        head2 = head2.next
        len2 -= 1
    
    # Move both pointers until they find the intersection or reach the end
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
    
    # Either head1 or head2 can be returned as they are equal at this point
    return head1 if head1 else None
