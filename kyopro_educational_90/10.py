N = int(input())
c1, c2 = [0], [0]

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        c1.append(p)
        c2.append(0)
    else:
        c1.append(0)
        c2.append(p)

C1, C2 = [0] * (N + 2), [0] * (N + 2)

for i in range(N + 1):
    C1[i + 1] = C1[i] + c1[i]
    C2[i + 1] = C2[i] + c2[i]

Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    print(C1[r + 1] - C1[l], C2[r + 1] - C2[l])
