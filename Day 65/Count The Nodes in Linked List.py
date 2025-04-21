https://my.newtonschool.co/playground/code/zkkggs4suaiy


def count_nodes(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count
