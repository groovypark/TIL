def solution(key, lock):
    def rotate_matrix(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

    def push_down_matrix(matrix):
        return [[matrix[i - 1][j] if i > 0 else 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def push_up_matrix(matrix):
        return [[matrix[i + 1][j] if i < len(matrix) - 1 else 0 for j in range(len(matrix[0]))] for i in
                range(len(matrix))]

    def push_right_matrix(matrix):
        return [[matrix[i][j - 1] if j > 0 else 0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def push_left_matrix(matrix):
        return [[matrix[i][j + 1] if j < len(matrix[0]) - 1 else 0 for j in range(len(matrix[0]))] for i in
                range(len(matrix))]

    def move(matrix, dy, dx):
        matrix = matrix
        if dy > 0:
            for _ in range(dy):
                matrix = push_up_matrix(matrix)
        else:
            for _ in range(abs(dy)):
                matrix = push_down_matrix(matrix)
        if dx > 0:
            for _ in range(dx):
                matrix = push_right_matrix(matrix)
        else:
            for _ in range(abs(dx)):
                matrix = push_left_matrix(matrix)
        return matrix

    def match(key, lock):
        result = [[lock[i][j] ^ key[i][j] if i < len(key) and j < len(key) else lock[i][j] for j in range(len(lock))]
                  for i in range(len(lock))]
        for line in result:
            for v in line:
                if v == 0:
                    return False
        return True

    lock_matrix = lock
    key = [[key[i][j] if i < len(key) and j < len(
        key) else 0 for j in range(len(lock))] for i in range(len(lock))]
    for _ in range(4):
        for dy in range(-len(key), len(key)):
            for dx in range(-len(key), len(key)):
                key_matrix = move(key, dy, dx)
                if match(key_matrix, lock_matrix):
                    return True
        lock_matrix = rotate_matrix(lock_matrix)

    return False
