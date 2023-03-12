h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]


def check(l):
    ret = set()
    x, y = 0, 0
    ret.add(A[x][y])
    for i in l:
        if i == "d":
            x += 1
        if i == "r":
            y += 1
        tmp = A[x][y]
        if tmp in ret:
            return False
        ret.add(tmp)
    return True


ans = 0
for bits in range(1 << (h + w - 2)):
    l = ""
    for j in range(h + w - 2):
        if (bits >> j) & 1:
            l += "d"
        else:
            l += "r"

    if l.count("d") == h - 1 and l.count("r") == w - 1:
        ans += check(l)
print(ans)
