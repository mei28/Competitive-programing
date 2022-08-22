h, w = map(int, input().split())

G = [[i for i in input()] for _ in range(h)]

i, j = 0, 0
visited = [[False] * w for _ in range(h)]
visited[i][j] = True
S = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}

while True:
    s = G[i][j]
    di, dj = S[s]
    ni, nj = i + di, j + dj

    if ni < 0 or h <= ni or nj < 0 or w <= nj:
        print(i + 1, j + 1)
        exit()
    else:
        if visited[ni][nj]:
            print(-1)
            exit()
        else:
            i, j = ni, nj
            visited[ni][nj] = True
