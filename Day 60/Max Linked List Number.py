https://my.newtonschool.co/playground/code/2gz75ury8dw3


def max_list(num1, num2):
    val1, val2 = 0, 0
    while num1:
        val1 = val1 * 10 + num1.value
        num1 = num1.next
    while num2:
        val2 = val2 * 10 + num2.value
        num2 = num2.next
    return max(val1, val2)
