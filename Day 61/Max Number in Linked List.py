https://my.newtonschool.co/playground/code/d938alt51f4p


def max_num(head):
    maxy = 0
    cur = 0
    while head:
        if head.value == -1:
            cur = 0
        else:
            cur = cur * 10 + head.value
            maxy = max(maxy, cur)
        head = head.next
    return maxy
