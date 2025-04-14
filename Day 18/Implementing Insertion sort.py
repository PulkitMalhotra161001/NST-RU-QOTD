https://my.newtonschool.co/playground/code/sg327u71q4pw


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        key = seq[i]
        j = i - 1
        while j >= 0 and key < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key
    return seq
