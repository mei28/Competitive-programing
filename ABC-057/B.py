N, M = map(int, input().split())

A, B, C, D = [], [], [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for _ in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

for i in range(N):
    a, b = A[i], B[i]

    min_diff = 9999999999
    for j in range(M):
        c, d = C[j], D[j]

        diff = abs(a - c) + abs(b - d)
        if diff < min_diff:
            min_diff = diff
            ans = j + 1
    print(ans)
