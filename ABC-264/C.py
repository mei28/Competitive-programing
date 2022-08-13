from itertools import combinations

h1, w1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h2)]
_B = []

for b in B:
    for _b in b:
        _B.append(_b)


rows = list(combinations(range(h1), h2))
cols = list(combinations(range(w1), w2))


def make_mat(rs, cs):
    ret = []
    for r in rs:
        for c in cs:
            ret.append(A[r][c])
    return ret


for rs in rows:
    for cs in cols:
        _A = make_mat(rs, cs)

        if _A == _B:
            print("Yes")
            exit()

print("No")
