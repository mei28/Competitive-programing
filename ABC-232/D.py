h,w = map(int,input().split())
C = [input() for _ in range(h)]

dp = [[0]*(w+1) for _ in range(h+1)]

# for i in range(h+1):
#     dp[i][0] =1
# for i in range(w+1):
#     dp[0][i] =1
dp[1][1] = 1


for i in range(1,h+1):
    for j in range(1,w+1):
        if C[i-1][j-1]=='#':
            dp[i][j] = 0
            continue
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+1

ans = 0
flg = False
k = w+1

for i in range(1,h+1):
    for j in range(1,w+1):
        if dp[i][j] == 0:
            k = min(k,j)
            continue
        if k<j or k==1:
            continue
        ans = max(dp[i][j],ans)
    flg = False

# for d in dp:
#     print(d)
print(ans)
