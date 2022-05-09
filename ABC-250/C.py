n, q = map(int, input().split())
A = list(range(n + 1))
idx = list(range(n + 1))

for _ in range(q):
    x = int(input())
    fi = idx[x]
    si = fi + 1 if fi != n else fi - 1
    y = A[si]

    A[fi], A[si] = A[si], A[fi]
    idx[x], idx[y] = si, fi

print(*A[1:])
