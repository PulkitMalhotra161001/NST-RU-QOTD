https://my.newtonschool.co/playground/code/g4gxzdtxoib3


def is_palindrome(node):
    values = []
    temp = node
    while temp is not None:
        values.append(temp.val)
        temp = temp.next

    return values == values[::-1]

def insert(head, val):
    if head is None:
        return Node(val)
    else:
        cur = insert(head.next, val)
        head.next = cur
        return head
