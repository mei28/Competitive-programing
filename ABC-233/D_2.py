n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i] + A[i]

ans = 0
for i in range(1,n+1):
    for j in range(0,n-i+1):
        tmp = S[j+i]-S[j]

        if tmp == k:
            ans += 1

print(ans)
