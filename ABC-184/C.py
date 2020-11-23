r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def ok(a, b, c, d):
    if a + b == c + d:
        return True
    if a - b == c - d:
        return True
    if abs(a - c) + abs(b - d) <= 3:
        return True
    return False


if (r1, c1) == (r2, c2):
    print(0)
    exit()

if ok(r1, c1, r2, c2):
    print(1)
    exit()

if (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
    exit()

for i in range(-4, 5):
    for j in range(-4, 5):
        r3, c3 = r1+i, c1+j
        if ok(r1, c1, r3, c3) and ok(r3, c3, r2, c2):
            print(2)
            exit()

print(3)
