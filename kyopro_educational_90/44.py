N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift = 0
for i in range(Q):
    t, x, y = map(int, input().split())

    if t == 1:
        x -= 1
        y -= 1
        A[(x + shift) % N], A[(y + shift) % N] = A[(y + shift) % N], A[(x + shift) % N]
    elif t == 2:
        shift = (shift + N - 1) % N
    elif t == 3:
        x -= 1
        print(A[(x + shift) % N])
