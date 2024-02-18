import math

n, k = map(int, input().split())
A = list(map(int, input().split()))
XY = [[]]
for _ in range(n):
    x, y = map(int, input().split())
    XY.append([x, y])

T = []
for i in range(1, n + 1):
    xi, yi = XY[i]
    tmp = []
    for a in A:
        if i in A:
            break
        xa, ya = XY[a]
        diff = (xi - xa) ** 2 + (yi - ya) ** 2
        diff = diff**0.5
        tmp.append(diff)
    tmp.sort()
    if tmp != []:
        T.append(tmp)

ans = -1
for t in T:
    ans = max(min(t), ans)

print(ans)
