from typing import Counter

n, k = map(int, input().split())
C = list(map(int, input().split()))

cnter = Counter()
for ke in C:
    str_k = str(ke)
    cnter[str_k] += 1

keys = cnter.keys()

dct = Counter()
for ke in keys:
    dct[ke] = 0

for ke in C[0:k]:
    dct[str(ke)] += 1

ans = 0

pre = C[0]
for ke, v in dct.items():
    ans += v

for i in range(k, n):
    now = C[i]
    pre = C[i - k]

    dct[now] += 1
    dct[pre] -= 1
