N,K = map(int,input().split())
P = list(map(int,input().split()))

S = [0] * (N+1)
for i,p in enumerate(P):
    S[i+1] = S[i] + (P[i]+1)

ans = 0

res=0
for i in range(N):
    if i+K<=N:
        res = max(res, S[i+K]-S[i])

print(res/2)
