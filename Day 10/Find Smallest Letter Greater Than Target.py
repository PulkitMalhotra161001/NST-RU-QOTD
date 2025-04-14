https://my.newtonschool.co/playground/code/solwady4mjvz


def nextGreatestLetter(letters, y):
    s = set(letters)
    sorted_s = sorted(s)
    for char in sorted_s:
        if char > y:
            return char
    return sorted_s[0]
