n, m, l = map(int, input().split())
p, q, r = map(int, input().split())

ans = 0

A = [
    [(n, p), (m, q), (l, r)],
    [(n, p), (m, r), (l, q)],
    [(n, q), (m, r), (l, p)],
    [(n, q), (m, p), (l, r)],
    [(n, r), (m, p), (l, q)],
    [(n, r), (m, q), (l, p)],
]

for i in range(len(A)):
    tmp = 1
    for a, b in A[i]:
        tmp *= a // b

    ans = max(ans, tmp)

print(ans)
