from collections import defaultdict 
n = int(input())
A = list(map(int,input().split()))
q = int(input())
Qs = [list(map(int,input().split())) for _ in range(q)]


def get_dct(A):
    dct = {}
    for a in A:
        dct[a] = 0
    return dct

S = [get_dct(A) for _ in range(n+1)] 


for i in range(n):
    a = A[i]
    for k in S[i].keys():
        if k==a:
            S[i+1][a] = S[i][a] + 1
        else:
            S[i+1][k] = S[i][k]

for l,r,x in Qs:
    if not x in S[0].keys():
        print(0)
        continue
    print(S[r-1][x]-S[l-1][x])
