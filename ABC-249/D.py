n = int(input())
A = list(map(int, input().split()))

dct = {}
for a in A:
    dct[a] = dct.setdefault(a, 0) + 1
keys = [k for k in dct.keys()]
m = len(keys)
keys.sort()


ans = 0
for i in range(m - 2):
    for j in range(i, m - 1):
        a = keys[i]
        b = keys[j]
        c = a * b
        if c > keys[-1]:
            continue
        if c in keys:
            if a != b:
                ans += dct[a] * dct[b] * dct[c]
            elif a == b and b != c:
                ans += dct[a] * (dct[a] - 1) * dct[c]
            elif a != b and b == c:
                ans += dct[a] * dct[b] * (dct[b] - 1)
            else:
                ans += dct[b] * (dct[b] - 2) * (dct[b] - 1)

print(ans * 2)
