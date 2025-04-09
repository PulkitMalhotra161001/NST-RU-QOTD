https://my.newtonschool.co/playground/code/k60guj8emr3x


def findMid(head) :
    slow = fast = head
    if not head :
        return -1
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
    return slow.data
