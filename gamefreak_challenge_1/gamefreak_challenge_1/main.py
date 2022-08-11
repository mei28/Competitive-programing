import sys
from collections import deque

board = None
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
h, w = -1, -1


def main(lines):
    step = int(lines[0])
    global h, w
    h, w = map(int, lines[1].split(" "))
    global board
    board = [list(l) for l in lines[2:]]

    if step == 1:
        do_1()
    if step == 2:
        do_2()


def do_1():
    Ay, Ax = get_pos("A")
    By, Bx = get_pos("B")
    walk_cnt = Bx - Ax
    player_cnt = board[0].count("S")
    print(walk_cnt, player_cnt)


def do_2():
    Ay, Ax = get_pos("A")
    By, Bx = get_pos("B")
    dist = [[-1] * w for _ in range(h)]
    dist[Ay][Ax] = 0
    prev_x = [[-1] * w for _ in range(h)]
    prev_y = [[-1] * w for _ in range(h)]

    que = deque()
    que.append([Ay, Ax])

    while len(que) > 0:
        cy, cx = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            if not board[ny][nx] in [".", "A", "B"]:
                continue

            if dist[ny][nx] == -1:
                que.append([ny, nx])
                dist[ny][nx] = dist[cy][cx] + 1
                prev_x[ny][nx] = cx
                prev_y[ny][nx] = cy

    y, x = By, Bx
    visited_point = []
    walk_cnt = 0
    # show_board(board)
    while x != -1 and y != -1:
        visited_point.append([y, x])
        if y == Ay and x == Ax:
            break
        walk_cnt += 1
        py = prev_y[y][x]
        px = prev_x[y][x]
        x = px
        y = py

    player_cnt = 0
    player_pos_dct = {"E": [], "S": [], "W": [], "N": []}
    for i in range(h):
        for j in range(w):
            if board[i][j] in ["E", "S", "W", "N"]:
                player_cnt += 1
                player_pos_dct[board[i][j]].append([i, j])
    watched_pos = [[] for _ in range(player_cnt)]
    for k, v in player_pos_dct.items():
        if k == "E":
            for p in v:
                py, px = p
                for i in range(px, w):
                    watched_pos.append([py, i])
        if k == "W":
            for p in v:
                py, px = p
                for i in range(0, px):
                    watched_pos.append([py, i])
        if k == "N":
            for p in v:
                py, px = p
                for i in range(0, py):
                    watched_pos.append([i, px])

        if k == "S":
            for p in v:
                py, px = p
                for i in range(py, h):
                    watched_pos.append([i, px])
    battle_cnt = 0
    for vp in visited_point:
        if vp in watched_pos:
            battle_cnt = 1

    print(walk_cnt, battle_cnt)
    pass


def show_board(board):
    print("-" * 20)
    for i in board:
        print(i)
    print("-" * 20)


def get_pos(target: str) -> tuple:
    global board
    _h, _w = len(board), len(board[0])
    for i in range(_h):
        try:
            j = board[i].index(target)
            return i, j
        except:
            continue


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
