from itertools import combinations, permutations

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

P = [1] * (h - 1) + [0] * (w - 1)

# 0 -> 右 1->した
def check(l):
    x, y = 0, 0
    ret = set()
    ret.add(A[x][y])
    for i in l:
        if i == 0:
            x += 1
        if i == 1:
            y += 1
        if A[x][y] in ret:
            return False
        ret.add(A[x][y])

    return True


ans = 0
L = set(permutations(P))
print(len(L))
for l in L:
    if check(l):
        ans += 1
print(ans)
