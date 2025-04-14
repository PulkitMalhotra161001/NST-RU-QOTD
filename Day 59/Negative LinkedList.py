https://my.newtonschool.co/playground/code/ijapamzrnwbb


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
def isPositive(head):
    count = 0
    while head:
        if head.data  <= 0:
            count += 1
        head = head.next
    if(count&1):
        return "No"
    else:
        return "Yes"
        


