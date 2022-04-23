n, k = map(int, input().split())
Ss = [input() for _ in range(n)]


def count(dct):
    ret = 0
    for _, v in dct.items():
        if v == k:
            ret += 1

    return ret


m = 0
for bits in range(1 << n):
    dct = dict()
    for j in range(n):
        if bits >> j & 1:
            tmp = Ss[j]
            for s in tmp:
                dct[s] = dct.setdefault(s, 0) + 1

    m = max(m, count(dct))

print(m)
