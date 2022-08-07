n, m = map(int, input().split())

ans = []

for bits in range(1 << m):
    tmp = []
    for j in range(m):
        if (bits >> j) % 2 == 1:
            tmp.append(j + 1)

    if len(tmp) == n:
        ans.append(tmp)

ans.sort()

for a in ans:
    print(*a)
