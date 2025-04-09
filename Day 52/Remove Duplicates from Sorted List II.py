https://my.newtonschool.co/playground/code/092opk2f271p


"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

def deleteDuplicates(head):
    dummy = Node(0)  # Create a dummy node to handle edge cases easily
    dummy.next = head  # Link dummy to the head
    prev = dummy  # Use 'prev' to keep track of the last node before potential duplicates

    while head:
        # If current node is a start of a duplicates sequence
        if head.next and head.data == head.next.data:
            # Skip all duplicates
            while head.next and head.data == head.next.data:
                head = head.next
            # Link prev node to the node after the last duplicate
            prev.next = head.next
        else:
            # If current node is not a duplicate, just move prev to this node
            prev = prev.next
        
        # Move to the next node
        head = head.next

    return dummy.next  
