N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

D_dct = {}
T_dct = {}
for d in D:
    D_dct[d] = D_dct.setdefault(d,0) + 1

for t in T:
    T_dct[t] = T_dct.setdefault(t,0)+1
    D_dct[t] = D_dct.setdefault(t,0)

for k,v in T_dct.items():
    if D_dct[k] == 0 or D_dct[k]<v:
        print('NO')
        exit()
print('YES')
