n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i] + A[i]

ans = 0
left = 0
right = 0
flg = False
for i in range(1,n+1):
    for j in range(0,n-i+1):
        tmp = S[j+i]-S[j]

        if tmp == k:
            left = j
            right = j+i
            flg = True
            break
            
    if flg:
        break

tmp = S[right]-S[left]
for l in range(left,n):
    while right < n and tmp + A[right]<=k:
        tmp += A[right]
        right += 1
    
    if tmp == k:
        ans += 1
    tmp -= A[left]

print(ans)

