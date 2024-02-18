n = int(input())
ABCD = [list(map(int, input().split())) for _ in range(n)]

MAX = 110

T = [[0] * MAX for _ in range(MAX)]

for a, b, c, d in ABCD:
    T[c][a] += 1
    T[c][b] -= 1
    T[d][a] -= 1
    T[d][b] += 1


for y in range(MAX):
    for x in range(1, MAX):
        T[y][x] += T[y][x - 1]

for y in range(1, MAX):
    for x in range(MAX):
        T[y][x] += T[y - 1][x]


cnt = 0
for h in range(MAX):
    for w in range(MAX):
        cnt += 1 if T[h][w] > 0 else 0
print(cnt)
