n = int(input())
A = list(map(int, input().split()))

dct = {}
for a in A:
    dct[a] = dct.setdefault(a, 0) + 1
keys = [k for k in dct.keys()]
keys.sort()
m = len(keys)
ans = 0
for i in range(m):
    for j in range(m):
        q = keys[i]
        r = keys[j]
        if q * r > keys[-1]:
            break
        ans += dct.setdefault(q, 0) * dct.setdefault(r, 0) * dct.setdefault(q * r, 0)


print(ans)
