import bisect

n = int(input())

A = []
B = []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(a + b)


def compress(a, b):
    vals = []
    N = len(a)
    for i in range(N):
        for d in range(0, 2):
            ta = a[i] + d
            tb = b[i] + d

            vals.append(ta)
            vals.append(tb)

    vals.sort()
    vals = list(set(vals))

    for i in range(n):
        a[i] = bisect.bisect_left(vals, a[i])
        b[i] = bisect.bisect_left(vals, b[i])
    return a, b, vals


a, b, vals = compress(A, B)

N = max(max(a), max(b))
imos = [0] * (N + 1)

for i in range(n):
    imos[a[i]] += 1
    imos[b[i]] -= 1

for i in range(N):
    if 0 < i:
        imos[i] += imos[i - 1]

ans = []
print(a, b, vals, imos)

dct = {k: 0 for k in range(n)}

for i in range(len(imos)):
    im = imos[i]

print(*ans)
