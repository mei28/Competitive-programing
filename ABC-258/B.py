n = int(input())
A = [list(input()) for _ in range(n)]

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def check(sx, sy, nx, ny):
    ans = [A[sy][sx]]
    cnt = int(A[sy][sx])
    for _ in range(n - 1):
        sx, sy = sx + nx, sy + ny
        if sx < 0:
            sx = n - 1
        if sy < 0:
            sy = n - 1
        if sx >= n:
            sx = 0
        if sy >= n:
            sy = 0
        ans.append(A[sy][sx])
        cnt += int(A[sy][sx])

    return ans, cnt


ma = -1
ret = []
for sx in range(n):
    for sy in range(n):
        for i in range(8):
            nx, ny = dx[i], dy[i]
            ans, cnt = check(sx, sy, nx, ny)

            ret.append(ans)

rets = ["".join(t) for t in ret]
rets = sorted(rets, reverse=True)
# print(rets)
print(rets[0])
