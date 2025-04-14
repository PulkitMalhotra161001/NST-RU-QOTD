https://my.newtonschool.co/playground/code/ah4b3udrip59


def bag_of_tokens_score(tokens, power):
    tokens.sort()
    n = len(tokens)
    score = 0
    max_score = 0
    left = 0
    right = n - 1
    
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break
    
    return max_score

if __name__ == "__main__":
    N = int(input())
    assert 0 <= N <= 100000
    A = list(map(int,input().split(' ')))
    assert len(A) == N
    assert 0 <= min(A) and max(A) <= 10000
    power = int(input())
    assert 0 <= power <= 10000
    
    # Calculate and print the maximum score
    print(bag_of_tokens_score(A, power))
