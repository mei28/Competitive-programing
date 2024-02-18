import time


def process(x, y):
    s = {C[x][y]}
    dct = {C[x][y]: 0}
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= x + i < n and 0 <= y + j < n:
                s.add(C[x + i][y + j])
                dct[C[x + i][y + j]] = dct.setdefault(C[x + i][y + j], 0) + 1
    if dct[C[x][y]] > 6:
        return
    elif len(s) == 1 or (len(s) == 2 and 0 in s):
        C[x][y] = 0


def spiral_order(matrix):
    if not matrix:
        return []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_idx = 0

    row_start, row_end, col_start, col_end = 0, len(matrix), 0, len(matrix[0])
    while row_start < row_end and col_start < col_end:
        for _ in range(2):
            if dir_idx == 0:  # right
                for i in range(col_start, col_end):
                    process(row_start, i)
                row_start += 1

            elif dir_idx == 1:  # down
                for i in range(row_start, row_end):
                    process(i, col_end - 1)
                col_end -= 1

            elif dir_idx == 2:  # left
                for i in range(col_end - 1, col_start - 1, -1):
                    process(row_end - 1, i)
                row_end -= 1

            elif dir_idx == 3:  # up
                for i in range(row_end - 1, row_start - 1, -1):
                    process(i, col_start)
                col_start += 1

            dir_idx = (dir_idx + 1) % 4


if __name__ == "__main__":
    n, m = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(n)]

    for i in range(2):
        spiral_order(C)

    for row in C:
        print(" ".join(map(str, row)))
