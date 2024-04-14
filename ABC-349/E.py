import sys

sys.setrecursionlimit(10**7)


def evaluate_board(board):
    lines = [
        board[0],
        board[1],
        board[2],  # 横ライン
        [board[0][0], board[1][0], board[2][0]],  # 縦ライン
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],  # 斜めライン
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if all(x == "T" for x in line):
            return "Takahashi"
        if all(x == "A" for x in line):
            return "Aoki"
    return None


def minimax(board, depth, is_maximizing, scores, Takahashi_score, Aoki_score):
    winner = evaluate_board(board)
    if winner:
        return winner  # 直接勝者を返す

    if depth == 0 or all(all(cell != " " for cell in row) for row in board):
        return (
            "Takahashi"
            if Takahashi_score > Aoki_score
            else "Aoki"
            if Aoki_score > Takahashi_score
            else "Draw"
        )

    if is_maximizing:
        best_result = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "T"
                    result = minimax(
                        board,
                        depth - 1,
                        False,
                        scores,
                        Takahashi_score + scores[i][j],
                        Aoki_score,
                    )
                    board[i][j] = " "
                    if result == "Takahashi":
                        return "Takahashi"
                    best_result = best_result or result
        return best_result
    else:
        best_result = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "A"
                    result = minimax(
                        board,
                        depth - 1,
                        True,
                        scores,
                        Takahashi_score,
                        Aoki_score + scores[i][j],
                    )
                    board[i][j] = " "
                    if result == "Aoki":
                        return "Aoki"
                    best_result = best_result or result
        return best_result


initial_board = [[" " for _ in range(3)] for _ in range(3)]
scores = [list(map(int, input().split())) for _ in range(3)]
result = minimax(initial_board, 9, True, scores, 0, 0)
print(result)  # 直接勝者の名前を出力
