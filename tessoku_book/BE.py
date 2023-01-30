n, q = map(int, input().split())
A = [0] + list(map(int, input().split()))

# dp[i][j]: 街iから2^j回移動した時の街の番号
# dp[i][0] = A[i]
# dp[i][j] = dp[dp[i][j-1]][j-1]

nxt = [[0] * 32 for _ in range(n + 1)]

for rank in range(32):
    for i in range(n + 1):
        if rank == 0:
            nxt[i][rank] = A[i]
        else:
            nxt[i][rank] = nxt[nxt[i][rank - 1]][rank - 1]


def calc(x, y):
    i = 0
    while y > 0:
        if y & 1:
            x = nxt[x][i]
        y >>= 1
        i += 1
    return x


for _ in range(q):
    x, y = map(int, input().split())
    print(calc(x, y))
