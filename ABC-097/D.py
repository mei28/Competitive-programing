h, w = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

ans = 0

A = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if A[i][j] == -1:
            continue
        ans += C[A[i][j]][1]

print(ans)
