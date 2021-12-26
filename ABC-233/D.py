from collections import Counter
n,k = map(int,input().split())
A = list(map(int,input().split()))

S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i] + A[i]

ans = 0
dct = Counter(S)
for i in range(1,n+1):
    ans += dct[S[i]-k]
    

print(ans)

