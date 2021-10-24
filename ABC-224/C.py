n = int(input())
X, Y = [], []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

cnt = 0

"""
3点が同一直線上にある
dx1/dy1 = dx2/dy2 => dx1*dy2 == dx2*dy1
"""
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            ix, iy = X[i], Y[i]
            jx, jy = X[j], Y[j]
            kx, ky = X[k], Y[k]

            dx1 = ix - jx
            dx2 = jx - kx
            dy1 = iy - jy
            dy2 = jy - ky

            if dx2 * dy1 == dx1 * dy2:
                cnt += 1

_all = n * (n - 1) * (n - 2) // 6

print(_all - cnt)
