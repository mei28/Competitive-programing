n = int(input())
ans = [[1] * n for _ in range(n)]

cnt = 1
for i in range(0, n, 2):
    for j in range(n):
        ans[i][j] = cnt
        cnt += 1
for i in range(1, n, 2):
    for j in range(n):
        ans[i][j] = cnt
        cnt += 1
for a in ans:
    print(*a)
