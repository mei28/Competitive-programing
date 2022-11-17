from bisect import bisect_left as bl

hdict = {}
wdict = {}

H, W, rnow, cnow = map(int, input().split())
N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    if r not in hdict:
        hdict[r] = []
    hdict[r].append(c)
    if c not in wdict:
        wdict[c] = []
    wdict[c].append(r)


for k in hdict:
    hdict[k].sort()

for k in wdict:
    wdict[k].sort()


Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)

    if d == "L":
        wall = 0
        if rnow in hdict:
            bli = bl(hdict[rnow], cnow)
            if bli > 0:
                wall = hdict[rnow][bli - 1]
        cnow = max(cnow - l, wall + 1)
    if d == "R":
        wall = W + 1
        if rnow in hdict:
            bli = bl(hdict[rnow], cnow)
            if bli < len(hdict[rnow]):
                wall = hdict[rnow][bli]
        cnow = min(cnow + l, wall - 1)
    if d == "U":
        wall = 0
        if cnow in wdict:
            bli = bl(wdict[cnow], rnow)
            if bli > 0:
                wall = wdict[cnow][bli - 1]
        rnow = max(rnow - l, wall + 1)
    if d == "D":
        wall = H + 1
        if cnow in wdict:
            bli = bl(wdict[cnow], rnow)
            if bli < len(wdict[cnow]):
                wall = wdict[cnow][bli]
        rnow = min(rnow + l, wall - 1)
    print(rnow, cnow)
