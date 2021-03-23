from itertools import combinations

N = int(input())

dct = dict()
march = ["M", "A", "R", "C", "H"]
for i in range(N):
    a = input()[0]
    if a in march:
        dct[a] = dct.setdefault(a, 0) + 1

keys = dct.keys()

keys_list = list(combinations(keys, 3))

ans = 0
for i in keys_list:
    a, b, c = i
    ans += dct[a] * dct[b] * dct[c]

print(ans)
