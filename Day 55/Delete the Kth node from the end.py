https://my.newtonschool.co/playground/code/en9x4utk4me8


def deleteElement(head, k):
    slow = fast = head

    # Move fast pointer k steps ahead
    for _ in range(k-1):
        if fast is None:
            return head  # k is greater than the length of the list
        fast = fast.next

    # If fast reaches the end of the list, delete the first element
    if fast is None:
        return head.next

    prev = None
    # Move both slow and fast pointers until fast reaches the end of the list
    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next

    # Delete the kth element from the end
    if prev:
        prev.next = slow.next
    else:
        head = head.next

    return head
