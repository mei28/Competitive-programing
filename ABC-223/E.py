def solve2(x: int, y: int, a: int, b: int) -> bool:
    ay = a // x + (a % x != 0)
    by = y - ay
    return b <= by * x


def solve(x: int, y: int, a: int, b: int, c: int) -> bool:
    ay = a // x + (a % x != 0)
    if ay >= y:
        return False
    return solve2(x, y - ay, b, c) or solve2(y - ay, x, b, c)


x, y, a, b, c = map(int, input().split())

ok = False

ok |= solve(x, y, a, b, c)
ok |= solve(x, y, b, c, a)
ok |= solve(x, y, c, a, b)
ok |= solve(y, x, a, b, c)
ok |= solve(y, x, b, c, a)
ok |= solve(y, x, c, a, b)

if ok:
    print("Yes")
else:
    print("No")
