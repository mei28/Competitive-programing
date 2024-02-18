h, w, n = map(int, input().split())
S = [[0] * (w + 5) for _ in range(h + 5)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    S[c + 1][d + 1] += 1
    S[a][b] += 1
    S[c + 1][b] -= 1
    S[a][d + 1] -= 1

for i in range(h + 1):
    for j in range(1, w + 1):
        S[i][j] += S[i][j - 1]
for i in range(1, h + 1):
    for j in range(w + 1):
        S[i][j] += S[i - 1][j]

for s in S[1 : h + 1]:
    print(*s[1 : w + 1])
