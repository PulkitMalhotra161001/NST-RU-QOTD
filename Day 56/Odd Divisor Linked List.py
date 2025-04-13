https://my.newtonschool.co/playground/code/xemo109tjo02


def construct_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        cur.next = Node(value)
        cur = cur.next
    return head
def odd_divisors_ll(N):
    arr = []
    i = 1
    while i * i <= N:
        val = i * i
        arr.append(val)
        i += 1
    head = construct_linked_list(arr)
    return head
