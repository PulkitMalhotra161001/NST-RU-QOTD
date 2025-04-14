https://my.newtonschool.co/playground/code/7lprgac8fuqy


def calculate_diagonal_sum(matrix):
    N = len(matrix)
    # Compute primary and secondary diagonal sums
    primary_diagonal_sum = sum(matrix[i][i] for i in range(N))
    secondary_diagonal_sum = sum(matrix[i][N - i - 1] for i in range(N))

    # Handle middle element for odd N
    if N % 2 == 1:
        common_element = matrix[N // 2][N // 2]
        total_sum = primary_diagonal_sum + secondary_diagonal_sum - common_element
    else:
        total_sum = primary_diagonal_sum + secondary_diagonal_sum

    return total_sum

