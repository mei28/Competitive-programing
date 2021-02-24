N = int(input())
A = map(int, input().split())
A = sorted(A, reverse=True)

dct = {}
for a in A:
    dct[a] = dct.setdefault(a, 0) + 1

lst = [0, 0]
for k, v in dct.items():
    if v >= 4:
        lst.append(k)
        lst.append(k)
    elif v >= 2:
        lst.append(k)
lst.sort()
print(lst[-1] * lst[-2])
