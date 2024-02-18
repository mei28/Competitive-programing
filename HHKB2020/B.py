H, W = map(int, input().split())
mat = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    line = input()
    for j, l in enumerate(line):
        mat[i][j] = l

cnt = 0

for i in range(H):
    for j in range(1, W):
        if mat[i][j - 1] == "." and mat[i][j] == ".":
            cnt += 1

for j in range(W):
    for i in range(1, H):
        if mat[i - 1][j] == "." and mat[i][j] == ".":
            cnt += 1

print(cnt)
