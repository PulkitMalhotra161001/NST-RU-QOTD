https://my.newtonschool.co/playground/code/rvhyl1eiry0h


def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    return prime
    
def process_primes():
    try:
        t = int(input())  # Read the number of test cases
        assert 1 <= t <= 100000  # Constraint for t

        arr = list(map(int, input().split()))
        assert len(arr) == t  # Ensure the input count matches t

        primes = sieve_of_eratosthenes(1000000)

        for num in arr:
            assert 1 <= num <= 1000000  # Constraint for A[i]
            if primes[num] == True:
                print(1, end = " ")
            else:
                print(0, end = " ")

    except AssertionError:
        print("Input constraint violated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_primes()
