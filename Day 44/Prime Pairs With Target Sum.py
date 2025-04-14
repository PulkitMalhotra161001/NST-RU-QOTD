https://my.newtonschool.co/playground/code/lz4mzw6t1crc


def findPrimePairs(n):
    prime = [True] * (n + 1)  # List to store whether a number is prime or not
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

    # Finding prime numbers using Sieve of Eratosthenes algorithm
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    
    ans = []  # List to store the pairs of prime numbers
    for i in range(2, n):
        j = n - i  # Finding the complement of i to make the sum n
        if prime[i] and prime[j] and i <= j:
            ans.append([i, j])  # Adding the pair to the result list
    
    return ans  # Returning the list of prime pairs
