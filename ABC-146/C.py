def count_digit(x):
    return sum(c.isdigit() for c in str(x))


def check(m):
    return a * m + b * count_digit(m)


if __name__ == "__main__":
    a, b, x = map(int, input().split())

    ok, ng = 0, 1000000001
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if check(mid) <= x:
            ok = mid
        else:
            ng = mid
    print(ok)
