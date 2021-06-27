import math

a, b, c, d = map(int, input().split())

if d * c - b <= 0:
    print(-1)
    exit()


else:
    ng = 0
    ok = 1 << 63

    while ok - ng > 1:
        mid = (ng + ok) // 2
        if a + b * mid <= d * mid * c:
            ok = mid
        else:
            ng = mid
    print(ok)
