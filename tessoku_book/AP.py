N, K = map(int, input().split())

cnt = [[0] * 210 for _ in range(210)]

for _ in range(N):
    A, B = map(int, input().split())
    cnt[A][B] += 1

for i in range(1, 210):
    for j in range(210):
        cnt[i][j] += cnt[i - 1][j]

for i in range(210):
    for j in range(1, 210):
        cnt[i][j] += cnt[i][j - 1]


ans = 0

K += 1
for i in range(101):
    for j in range(101):
        ans = max(
            ans, cnt[i + K][j + K] + cnt[i][j] - cnt[i][j + K] - cnt[i + K][j]
        )

print(ans)
