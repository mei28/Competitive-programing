import sys

# メモ key:(x,y,z)
memo = dict()


def rec(x: int, y: int, z: int) -> int:
    global memo

    for i in memo:
        print(i, memo[i])
    print("-"*20)

    k = (x, y, z)

    if x <= y:
        memo[k] = y
        return y
    if k in memo:
        return memo[k]

    memo[k] = rec(rec(x-1, y, z), rec(y-1, z, x), rec(z-1, x, y))

    return memo[k]


def T(x: int, y: int, z: int) -> int:

    global memo

    k = (x, y, z)

    if x <= y:
        memo[k] = y
    elif x > y and y <= z:
        memo[k] = z
    else:
        memo[k] = x
    return memo[k]


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    line = lines[0]
    x, y, z = map(int, line.split())
    # print(rec(x,y,z))
    print(T(x, y, z))
