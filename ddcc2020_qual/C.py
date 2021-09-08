h, w, k = map(int, input().split())

cake = [input() for _ in range(h)]
tab = [[-1] * w for i in range(h)]


def show_cake_cut():
    for i in tab:
        print(*i)


# イチゴに番号をつける
now = 1
for i in range(h):
    for j in range(w):
        if cake[i][j] == "#":
            tab[i][j] = now
            now += 1

# 自分が-1のとき左の文字を採用する
for i in range(h):
    for j in range(1, w):
        if tab[i][j] == -1:
            tab[i][j] = tab[i][j - 1]

# 自分が-1のとき右の文字を採用する
for i in range(h):
    for j in range(w - 2, -1, -1):
        if tab[i][j] == -1:
            tab[i][j] = tab[i][j + 1]

# 自分が-1のとき下の文字を採用する
for i in range(1, h):
    for j in range(w):
        if tab[i][j] == -1:
            tab[i][j] = tab[i - 1][j]


# 自分が-1のとき下の文字を採用する
for i in range(h - 2, -1, -1):
    for j in range(w):
        if tab[i][j] == -1:
            tab[i][j] = tab[i + 1][j]

show_cake_cut()
