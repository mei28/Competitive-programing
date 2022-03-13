n = int(input())

XY = [tuple(map(int,input().split())) for _ in range(n)]

S = list(input())
A = []
for s,(x,y) in zip(S,XY):
    A.append((x,y,s))

A = list(sorted(A,key=lambda x:(x[1],x[0])))

dct = {}
for x,y,s in A:
    if not y in dct.keys():
        dct[y] = []
    dct[y].append((x,s))


for v in dct.values():
    tmp = ''
    r_flg = False
    for _,e in v:
        if e=='R':
            r_flg = True
        if e=='L' and r_flg:
            print('Yes')
            exit()

print("No")
