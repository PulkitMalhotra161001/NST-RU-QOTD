https://my.newtonschool.co/playground/code/kse3xhsc29s6


from collections import deque

def count_students_unable_to_eat(students, sandwiches):
    queue = deque(students)
    stack = list(sandwiches)
    rotations = 0

    while queue and rotations < len(queue):
        if queue[0] == stack[0]:
            queue.popleft()
            stack.pop(0)
            rotations = 0
        else:
            queue.append(queue.popleft())
            rotations += 1

    return len(queue)

def main():
    n = int(input().strip())
    students = list(map(int, input().strip().split()))
    sandwiches = list(map(int, input().strip().split()))

    assert 1 <= n <= 100
    assert len(students) == len(sandwiches) == n
    assert all(x in [0, 1] for x in students)
    assert all(x in [0, 1] for x in sandwiches)

    result = count_students_unable_to_eat(students, sandwiches)
    print(result)

if __name__ == "__main__":
    main()
