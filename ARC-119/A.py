def is_ok(q, m):
    if 2 ** m > q:
        return True
    else:
        return False


def binary_search(q: int):
    ok = 0
    ng = 60

    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(q, mid):
            ng = mid
        else:
            ok = mid
    return ok


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(1)
        exit()
    b_max = binary_search(N)
    min_abc = 1 << 60
    for b in range(b_max):
        a = N // (2 ** b)
        c = N - 2 ** b * a
        min_abc = min(min_abc, a + b + c)
    print(min_abc)
