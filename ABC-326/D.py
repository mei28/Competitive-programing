from itertools import permutations, product


def is_valid(board, R, C):
    N = len(board)

    for i in range(N):
        col = [board[j][i] for j in range(N)]
        if col.count("A") > 1 or col.count("B") > 1 or col.count("C") > 1:
            return False

    col_flg = [False] * 5
    row_flg = [False] * 5
    cols = ["."] * 5
    rows = ["."] * 5
    for i in range(5):
        for j in range(5):
            if board[i][j] != ".":
                if not col_flg[j]:
                    col_flg[j] = True
                    cols[j] = board[i][j]
    for j in range(5):
        for i in range(5):
            if board[i][j] != ".":
                if not row_flg[i]:
                    row_flg[i] = True
                    rows[i] = board[i][j]
    if "".join(rows) == R and "".join(cols) == C:
        return True
    return False


def solve(N, R, C):
    base_pattern = [".", ".", "A", "B", "C"]
    perms = list(permutations(base_pattern, N))
    for board in product(perms, repeat=5):
        print(board)
        if is_valid(board, R, C):
            return board
    return None


N = int(input())
R = input()
C = input()

solution = solve(N, R, C)
if solution:
    for row in solution:
        print("".join(row))
else:
    print(-1)
