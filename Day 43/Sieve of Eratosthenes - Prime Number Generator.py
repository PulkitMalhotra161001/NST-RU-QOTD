https://my.newtonschool.co/playground/code/y8qbycaqtoyh


def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes

n = int(input())
assert 1 <= n <= 1000000
ans = sieve_of_eratosthenes(n)
print(*ans)
    
