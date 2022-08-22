n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))

y, z, w = 0, 0, 0
s0, s1, s2 = 0, 0, 0
ok = 0

for x in range(n):
    while y < n and s0 < p:
        s0 += A[y]
        s1 -= A[y]
        y += 1

    while z < n and s1 < q:
        s1 += A[z]
        s2 -= A[z]
        z += 1
    while w < n and s2 < r:
        s2 += A[w]
        w += 1

    if s0 == p and s1 == q and s2 == r:
        ok = 1
        break

    s0 -= A[x]

print("Yes" if ok else "No")
