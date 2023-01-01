h, w = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(h)]
S = [[0] * (w + 10) for _ in range(h + 10)]

for i in range(h):
    for j in range(w):
        S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + X[i][j]

q = int(input())

for _ in range(q):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    print(S[c + 1][d + 1] - S[c + 1][b] - S[a][d + 1] + S[a][b])
