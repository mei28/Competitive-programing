x, y, z = map(int, input().split())

if y < 0:
    x *= -1
    y *= -1
    z *= -1
if x < y:
    print(abs(x))
else:
    if z > y:
        print(-1)
    else:
        print(abs(z) + abs(x - z))
