H, W, X, Y = map(int, input().split())
S = [["" for _ in range(W)] for _ in range(H)]

for i in range(H):
    line = input()
    for j, l in enumerate(line):
        S[i][j] = l

cnt = 0

X, Y = X - 1, Y - 1
# right
x, y = X, Y

while True:
    if 0 <= y < W and 0 <= x < H:
        if S[x][y] == ".":
            cnt += 1
        else:
            break
    else:
        break
    x += 1
x, y = X, Y
while True:
    if 0 <= y < W and 0 <= x < H:
        if S[x][y] == ".":
            cnt += 1
        else:
            break
    else:
        break
    x -= 1
x, y = X, Y
while True:
    if 0 <= y < W and 0 <= x < H:
        if S[x][y] == ".":
            cnt += 1
        else:
            break
    else:
        break
    y += 1
x, y = X, Y
while True:
    if 0 <= y < W and 0 <= x < H:
        if S[x][y] == ".":
            cnt += 1
        else:
            break
    else:
        break
    y -= 1

x, y = X, Y
if S[x][y] == ".":
    cnt -= 3
print(cnt)
