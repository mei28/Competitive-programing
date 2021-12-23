n = int(input())
W = list(map(int, input().split()))
W.sort()

# dp[i][j] i種類使って差をjにすることができるか
dp = [[False] * (sum(W) + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    for j in range(sum(W) + 1):
        if not dp[i][j]:
            continue
        dp[i + 1][j + W[i]] = True
        dp[i + 1][abs(j - W[i])] = True

for i in range(sum(W) + 1):
    # print(dp[n])
    if dp[n][i]:
        print(i)
        exit()
