import math

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

G = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]

cnt = 0
for i, j, k in [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]:
    l = G[i]
    m = G[j]
    n = G[k]

    a = [l[0] - m[0], l[1] - m[1]]
    b = [n[0] - m[0], n[1] - m[1]]

    costh = (a[0] * b[0] + a[1] * b[1]) / (
        math.sqrt((a[0] ** 2 + a[1] ** 2) * (b[0] ** 2 + b[1] ** 2))
    )
    arc = math.acos(costh)
    the = math.degrees(arc)
    the2 = 180 - the
    cnt += the
    # print(i, j, k, costh, math.degrees(arc))

if cnt < 360:
    print("No")
else:
    print("Yes")
