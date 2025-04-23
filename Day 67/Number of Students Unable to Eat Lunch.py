https://my.newtonschool.co/playground/code/63yoiq10at63


def count_students(students, sandwiches):
    a = [0, 0]  # a[0] -> count of students who want 0, a[1] -> count of students who want 1
    n = len(students)

    for student in students:
        a[student] += 1

    for k in range(n):
        if a[sandwiches[k]] > 0:
            a[sandwiches[k]] -= 1
        else:
            return n - k

    return 0


def main():
    # First line: number of students
    n = int(input().strip())

    # Second line: student preferences (0 or 1)
    students = list(map(int, input().strip().split()))

    # Third line: sandwich stack (0 or 1)
    sandwiches = list(map(int, input().strip().split()))

    print(count_students(students, sandwiches))


if __name__ == "__main__":
    main()
