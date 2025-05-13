https://my.newtonschool.co/playground/code/fsium311sq16


def node_position(head, X):
    pos = 1
    while head.value != X:
        head = head.next
        pos += 1
    return pos
