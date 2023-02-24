from itertools import combinations
from typing import Counter


S = [input() for _ in range(9)]


def check(a, b, c, d):
    ab = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    ac = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
    ad = (a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2
    cb = (c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2
    bd = (b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2
    cd = (c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2
    cnter = Counter([ab, ac, ad, cb, bd, cd])
    if len(cnter) == 2:
        return True
    return False


D = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            D.append([i, j])

n = len(D)

cnt = 0

for i, j, k, l in list(combinations(range(n), 4)):
    a, b, c, d = D[i], D[j], D[k], D[l]

    if check(a, b, c, d):
        cnt += 1
print(cnt)
