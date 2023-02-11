n, m = map(int, input().split())

B = []
for _ in range(m):
    _ = input()
    A = list(map(int, input().split()))
    B.append(A)

ans = 0
for bits in range(1 << m):
    tmp = set()
    for j in range(m):
        if (bits >> j) & 1:
            tmp |= set(B[j])
    if len(tmp) == n:
        ans += 1
print(ans)
