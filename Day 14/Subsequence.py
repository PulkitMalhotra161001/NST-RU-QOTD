https://my.newtonschool.co/playground/code/8nevdmfq1p8s


def generate_subsequences(s, index, current, subsequences):
    if index == len(s):
        if current:
            subsequences.append(current)
        return
    
    # Case 1: Include the current character
    generate_subsequences(s, index + 1, current + s[index], subsequences)
    
    # Case 2: Exclude the current character
    generate_subsequences(s, index + 1, current, subsequences)

def all_subsequences(s):
    subsequences = []
    generate_subsequences(s, 0, '', subsequences)
    subsequences.sort()  # Sort lexicographically
    return subsequences
