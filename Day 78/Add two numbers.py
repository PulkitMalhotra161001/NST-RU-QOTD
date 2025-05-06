https://my.newtonschool.co/playground/code/pug9xr3o8fzw


def addNumber(first, second):
    res = None
    prev = None
    temp = None
    carry = 0
    while first or second:
        sum_val = carry + (first.data if first else 0) + (second.data if second else 0)
        carry = 1 if sum_val >= 10 else 0
        sum_val = sum_val % 10
        temp = Node(sum_val)
        if not res:
            res = temp
        else:
            prev.next = temp
        prev = temp
        if first:
            first = first.next
        if second:
            second = second.next
    if carry > 0:
        temp.next = Node(carry)
    return res
