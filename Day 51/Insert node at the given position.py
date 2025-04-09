https://my.newtonschool.co/playground/code/xlsq0vmil6xf


def addElement(head, M, K):
    # Step 1: Create a new node to insert
    new_node = Node(K)
    
    # Step 2: If inserting at the head (M == 1)
    if M == 1:
        new_node.next = head
        return new_node  # The new node is now the head of the list
    
    # Step 3: Traverse to the (M-1)th position
    current = head
    position = 1  # Starting position (1-based indexing)
    
    while current is not None and position < M - 1:
        current = current.next
        position += 1

    # Step 4: Insert the new node at the M-th position
    if current is not None:
        new_node.next = current.next
        current.next = new_node

    return head
