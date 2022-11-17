h, w = map(int, input().split())
C = [input() for _ in range(h)]

si, sj = -1, -1

for i in range(h):
    for j in range(w):
        if C[i][j] == "S":
            si, sj = i, j

        if i + 1 < h and C[i][j] == C[i + 1][j] == ".":
            merge(i * w + j)
