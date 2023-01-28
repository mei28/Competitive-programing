q = int(input())
dct = {}
for _ in range(q):
    l = input().split()
    if l[0] == "1":
        x, y = l[1], int(l[2])
        dct[x] = y
    else:
        x = l[1]
        print(dct[x])
