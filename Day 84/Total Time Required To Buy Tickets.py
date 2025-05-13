https://my.newtonschool.co/playground/code/gnsfgwlm1tyq


def time_required(tickets, K):
    queue = deque()
    time = 0

    for i in range(len(tickets)):
        queue.append(i)

    while queue:
        index = queue.popleft()
        tickets[index] -= 1
        time += 1

        if tickets[index] == 0 and index == K:
            return time
        if tickets[index] > 0:
            queue.append(index)

    return time
