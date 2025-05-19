https://my.newtonschool.co/playground/code/fqe0bg2o4i04


def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    dvd = abs(dividend)
    dvs = abs(divisor)
    ans = 0
    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1

    while dvd >= dvs:
        temp = dvs
        m = 1
        while temp << 1 <= dvd:
            temp <<= 1
            m <<= 1
        dvd -= temp
        ans += m

    return sign * ans

def main():
    t = 1  # number of test cases, hardcoded as in C++ code
    for _ in range(t):
        n,m = map(int,input().split())
        print(divide(n, m))

if __name__ == "__main__":
    main()
