h,w = map(int,input().split())
C = [list(input()) for _ in range(h)]

dp = [[0]*(w+1) for _ in range(h+1)]

for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if C[i][j] == "#":
            continue

        dp[i][j] = max(dp[i+1][j],dp[i][j+1])+1

# for d in dp:
#     print(d)

print(dp[0][0])
