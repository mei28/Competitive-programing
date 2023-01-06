N = int(input())
PA = []

for _ in range(N):
    PA.append(list(map(int, input().split())))


dp = [[0] * (N + 1) for _ in range(N + 1)]


for width in range(N - 1, -1, -1):
    for l in range(N):
        r = l + width
        if r > N:
            break
        if l - 1 >= 0:
            p, a = PA[l - 1]
            p -= 1
            dp[l][r] = max(
                dp[l - 1][r] + (a if l - 1 <= p < r else 0), dp[l][r]
            )
        if r + 1 <= N:
            p, a = PA[r]
            p -= 1
            dp[l][r] = max(
                dp[l][r + 1] + (a if l <= p < r + 1 else 0), dp[l][r]
            )


print(max(dp[i][i] for i in range(N + 1)))
