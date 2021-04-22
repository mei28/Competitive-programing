H, W = map(int, input().split())

field = [input() for _ in range(H)]

cnt = 0
for i in range(H - 1):
    for j in range(W - 1):
        cnt += ((field[i][j] == '#')
                + (field[i][j + 1] == '#')
                + (field[i + 1][j] == '#')
                + (field[i+1][j+1] == '#')) % 2

print(cnt)
