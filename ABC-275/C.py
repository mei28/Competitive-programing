from collections import Counter
from itertools import combinations

S = [input() for _ in range(9)]


def check(a, b, c, d):
    ab = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    ac = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
    ad = (a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2
    db = (d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2
    dc = (d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2
    bc = (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
    cnter = Counter([ab, ac, ad, db, dc, bc])

    if len(cnter) == 2:
        return True
    return False


DOT = []

for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            DOT.append((i, j))
# DOT = list(sorted(DOT, key=lambda x: (x[0], x[1])))

n = len(DOT)
cnt = 0


for i, j, k, l in list(combinations(range(n), 4)):
    a, b, c, d = DOT[i], DOT[j], DOT[k], DOT[l]
    if check(a, b, c, d):
        cnt += 1
print(cnt)
