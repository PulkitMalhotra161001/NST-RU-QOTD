https://my.newtonschool.co/playground/code/wcvm75fls4ms


def count_inversions(list_of_numbers):
    swaps = 0
    for i in range(0, len(list_of_numbers)):
        for j in range(0, len(list_of_numbers) - i - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                swaps += 1
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
    return swaps
