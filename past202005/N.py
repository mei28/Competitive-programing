n, q = map(int, input().split())

A = [i + 1 for i in range(0, n)]

for i in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if t == 1:
        A[x + 1], A[x] = A[x], A[x + 1]
    else:
        A[x : y + 1] = list(sorted(A[x : y + 1]))

print(*A)
