n, h, w = map(int, input().split())
board = [[[0, 0, 0] for _ in range(w)] for _ in range(h)]

Q = []

for _ in range(n):
    q = []
    for _ in range(3):
        x, y, s = map(int, input().split())
        q.append((x, y, s))

    Q.append(q)


def check(_x, _y, i):
    if h <= _y or w <= _x:
        return
    board[_y][_x][i] = 1

    if sum(board[_y][_x]) >= 2:
        for j in range(3):
            board[_y][_x][j] = 1 - board[_y][_x][j]

    # print(board[_y][_x],_x,_y,i)
    assert sum(board[_y][_x]) <= 1


def cnt():
    a, b, c = 0, 0, 0

    for i in range(h):
        for j in range(w):
            tmp = board[i][j]
            if sum(tmp) == 0:
                continue
            idx = tmp.index(1)
            if idx == 0:
                a += 1
            elif idx == 1:
                b += 1
            elif idx == 2:
                c += 1

    print(a, b, c)


def view():
    print("=" * 20)
    colors = ["R", "B", "G", "N"]

    for i in range(h):
        for j in range(w):
            if sum(board[i][j]) == 0:
                print(colors[3], end="")
            else:
                print(colors[board[i][j].index(1)], end="")

        print()
    print("=" * 20)


for qs in Q:
    for i, (x, y, s) in enumerate(qs):
        for dx in range(s):
            for dy in range(s):
                check(x + dx, y + dy, i)
        # view()


cnt()
