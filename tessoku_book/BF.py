n, q = map(int, input().split())

seg = [0] * (1 << 22)


def add(pos, x):
    # 木の一番左
    pos += 1 << 20
    seg[pos] = x

    pos //= 2
    while pos:
        seg[pos] = max(seg[pos * 2], seg[pos * 2 + 1])
        pos //= 2


def get_max(l, r):
    l += 1 << 20
    r += 1 << 20

    ans = 0
    while l < r:
        if l % 2 == 1:
            ans = max(ans, seg[l])
            l += 1
        if r % 2 == 1:
            ans = max(ans, seg[r - 1])
            r -= 1
        l //= 2
        r //= 2
    return ans


for _ in range(q):
    query = input().split()
    if query[0] == "1":
        pos, x = int(query[1]), int(query[2])
        add(pos, x)
    else:
        l, r = int(query[1]), int(query[2])
        print(get_max(l, r))
