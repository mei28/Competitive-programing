n,q = map(int,input().split())
dct = {}
A = list(map(int,input().split()))

for i, x in enumerate(A):
    if x not in dct.keys():
        dct[x] = []

    dct[x].append(i+1)
for _ in range(q):
    x,k = map(int,input().split())

    if x not in dct.keys():
        print(-1)
    else:
        d = dct[x]
        if k > len(d):
            print(-1)
        else:
            print(d[k-1])
