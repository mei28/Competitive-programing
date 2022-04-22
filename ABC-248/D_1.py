n = int(input())
A = list(map(int,input().split()))
q = int(input())
Qs = [list(map(int,input().split())) for _ in range(q)]


D = [[0]*(n+2) for _ in range(max(A)+1)]

for i,a in enumerate(A):
    D[a][i+1] = 1

for d in D:
    for i in range(1,n+1):
        d[i+1] += d[i]

for l,r,x in Qs:
    d = D[x]
    print(d[r]-d[l-1])
