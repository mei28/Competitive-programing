n, q = map(int, input().split())
L = dict()

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in L.keys():
            L[a] = set()
        L[a].add(b)
    if t == 2:
        try:
            L[a].remove(b)
        except:
            continue
    if t == 3:
        if a not in L.keys() or b not in L.keys():
            print("No")
            continue
        if b in L[a] and a in L[b]:
            print("Yes")
        else:
            print("No")
