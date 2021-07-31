from collections import Counter

Q = int(input())


dct = dict()
up = 0
for _ in range(Q):
    ix = input()
    if ix[0] == "3":
        i = ix[0]
    else:
        i, x = map(int, ix.split())

    if i == 1:
        x = str(x)
        dct[x] = dct.setdefault(x, 0) + 1
    elif i == 2:
        if len(dct.keys()) == 0:
            continue
        up += x
    else:
        if up != 0:
            keys = list(dct.keys())
            keys.sort(reverse=True)
            for k in keys:
                k = int(k)
                dct[str(up + k)] = dct.setdefault(str(up + k), 0) + dct[str(k)]
                del dct[str(k)]
        up = 0
        key = list(dct.keys())[0]
        print(key)
        dct[key] -= 1
        if dct[key] == 0:
            del dct[key]
