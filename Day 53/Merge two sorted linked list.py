https://my.newtonschool.co/playground/code/kfpmngrblzj8


'''
	class Node:
		def __init__(self, data):  
		    self.data = data
		    self.next = None

'''
#Function to merge two sorted linked list.
def Merge(head1, head2):
    dummy_node = Node(-1)
    ptr = dummy_node
    
    cur1 = head1
    cur2 = head2
    
    while cur1 and cur2:
        if cur1.data < cur2.data:
            ptr.next = cur1
            cur1 = cur1.next
        else:
            ptr.next = cur2
            cur2 = cur2.next
        ptr = ptr.next
    
    if cur1:
        ptr.next = cur1
    elif cur2:
        ptr.next = cur2
    
    return dummy_node.next
