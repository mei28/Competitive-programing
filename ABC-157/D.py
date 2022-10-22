n, m, k = map(int, input().split())
F = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    F[a][b] = 1
    F[b][a] = 1
for _ in range(k):
    a, b = map(int, input().split())
    F[a][b] = -1
    F[b][a] = -1

for i in range(1, n + 1):
    cnt = F[i][1:].count(0)
    print(cnt - 1)
