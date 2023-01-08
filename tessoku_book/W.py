n, m = map(int, input().split())
AA = [list(map(int, input().split())) for _ in range(m)]

ans = 10**10
flg = False
for bits in range(1 << m):
    tmp = [0] * n
    cnt = 0
    for j in range(m):
        if (bits >> j) & 1:
            cnt += 1
            for i in range(n):
                tmp[i] |= AA[j][i]
    if all([a == 1 for a in tmp]):
        flg = True
        ans = min(ans, cnt)

print(ans if flg else -1)
