from collections import Counter
from itertools import product

n, x = map(int, input().split())

AA = []
L = []
for i in range(n):
    tmp = list(map(int, input().split()))
    l = tmp[0]
    a = tmp[1:]
    L.append(l)
    AA.append(Counter(a))

ans = 0

keys = []
for i in range(n):
    a = AA[i]
    tmp = []
    for k in a.keys():
        tmp.append(k)
    keys.append(tmp)
l_p = list(product(*keys))

ans = 0
for c in l_p:
    tmp = 1
    ans_tmp = 1
    for i, a in enumerate(c):
        tmp *= a
        ans_tmp *= AA[i][a]

    if tmp == x:
        ans += ans_tmp

print(ans)
