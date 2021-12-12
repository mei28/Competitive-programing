h, w = map(int, input().split())
mat = [input() for _ in range(h)]

left = [[0] * w for _ in range(h)]
right = [[0] * w for _ in range(h)]
top = [[0] * w for _ in range(h)]
bottom = [[0] * w for _ in range(h)]

for i in range(h):
    cur = 0
    for j in range(w):
        if mat[i][j] == "#":
            cur = 0
        else:
            cur += 1
        left[i][j] = cur

for i in range(h):
    cur = 0
    for j in range(w - 1, -1, -1):
        if mat[i][j] == "#":
            cur = 0
        else:
            cur += 1
        right[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h):
        if mat[i][j] == "#":
            cur = 0
        else:
            cur += 1

        bottom[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h - 1, -1, -1):
        if mat[i][j] == "#":
            cur = 0
        else:
            cur += 1

        top[i][j] = cur

ans = 0

for i in range(h):
    for j in range(w):
        if mat[i][j] == "#":
            continue
        ans = max(ans, left[i][j] + right[i][j] + top[i][j] + bottom[i][j] - 3)

print(ans)
