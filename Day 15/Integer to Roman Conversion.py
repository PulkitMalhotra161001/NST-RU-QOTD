https://my.newtonschool.co/playground/code/z6svqcyyfpgh


def intToRoman(num):
   
    if num >= 1000:
        return (num // 1000) * 'M' + intToRoman(num % 1000)
    elif num >= 500:
        if (num // 100) == 9:
            return 'CM' + intToRoman(num % 100)
        else:
            return 'D' + intToRoman(num - 500)
    elif num >= 100:
        if (num // 100) == 4:
            return 'CD' + intToRoman(num % 100)
        else:
            return (num // 100) * 'C' + intToRoman(num % 100)
    elif num >= 50:
        if (num // 10) == 9:
            return 'XC' + intToRoman(num % 10)
        else:
            return 'L' + intToRoman(num - 50)
    elif num >= 10:
        if (num // 10) == 4:
            return 'XL' + intToRoman(num % 10)
        else:
            return (num // 10) * 'X' + intToRoman(num % 10)
    elif num >= 5:
        if num == 9:
            return 'IX'
        else:
            return 'V' + intToRoman(num - 5)
    else:
        if num == 4:
            return 'IV'
        elif num == 0: 
            return ''
        else:
            return num * 'I'


if __name__ == '__main__':
    n = int(input())
    res = intToRoman(n)
    print(res)
