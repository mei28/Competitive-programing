n = int(input())

P = []
for i in range(n):
    t, l, r = map(int, input().split())
    P.append((t, l, r))


def xy(t, l, r):
    if t == 1:
        return l, r
    elif t == 2:
        return l, r - 0.5
    elif t == 3:
        return l + 0.5, r
    else:
        return l + 0.5, r - 0.5


cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        t1, l1, r1 = P[i]
        t2, l2, r2 = P[j]

        l1, r1 = xy(t1, l1, r1)
        l2, r2 = xy(t2, l2, r2)
        cnt += max(l1, l2) <= min(r1, r2)
print(cnt)
