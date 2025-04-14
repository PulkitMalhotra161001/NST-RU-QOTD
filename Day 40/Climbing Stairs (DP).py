https://my.newtonschool.co/playground/code/19d2zkvtf4tn


def count_ways(n, memo):
    MOD = 10**9 + 7
    
    # Base cases
    if n == 0:
        return 1  # There's one way to stand at the bottom without climbing.
    if n < 0:
        return 0  # No way to climb negative steps.
    
    # If already calculated, return stored result
    if memo[n] != -1:
        return memo[n]
    
    # Recursive relation
    memo[n] = (count_ways(n - 1, memo) + count_ways(n - 2, memo)) % MOD
    return memo[n]

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    # Initialize memoization array
    memo = [-1] * (n + 1)
    
    # Get result
    result = count_ways(n, memo)
    print(result)

if __name__ == "__main__":
    main()
