Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

G = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]


# cross product: (b - a)×(c - a)
def cross3(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# O(N)
def inside_convex_polygon0(p0, qs):
    L = len(qs)
    D = [cross3(qs[i - 1], p0, qs[i]) for i in range(L)]
    return all(e >= 0 for e in D) or all(e <= 0 for e in D)


# O(log N)
def inside_convex_polygon(p0, qs):
    L = len(qs)
    left = 1
    right = L
    q0 = qs[0]
    while left + 1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L - 1:
        left -= 1
    qi = qs[left]
    qj = qs[left + 1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1
        v2 = -v2
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0


cnt = 0
qs = G.copy()
for i, j, k, a in [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]]:
    l = G[i]
    m = G[j]
    n = G[k]
    b = G[a]
    qs = [l, m, n]
    if inside_convex_polygon(b, qs):
        print("No")
        exit()
print("Yes")
