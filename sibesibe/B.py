A = [list(map(int, input().split())) for _ in range(4)]

di = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for i in range(4):
    for j in range(4):
        flg = False
        for dx, dy in di:
            if i + dx < 0 or 4 <= i + dx or j + dy < 0 or 4 <= j + dy:
                continue

            if A[i][j] == A[i + dx][j + dy]:
                print("CONTINUE")
                exit()


print("GAMEOVER")
