https://my.newtonschool.co/playground/code/px9ymgmd6f0l


def trailingZeroes(N):
    return N // 5 + trailingZeroes(N // 5) if N >= 5 else 0
