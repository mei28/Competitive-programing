N = int(input())
S = [int(input()) for _ in range(N)]

dp = [0] * (sum(S)+1)

dp[0] = 1

for i in range(N):
    for j in range(len(dp) - 1, -1, -1):
        if dp[j] == 1:
            dp[j+S[i]] = 1

ans = 0 
for i in range(len(dp)):
    if dp[i] == 1 and i % 10 != 0:
        ans =i 
print(ans)
