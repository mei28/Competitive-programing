N, S = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[i][j]: i日までにj円かどうか
dp = [[False for _ in range(S + 10)] for _ in range(N + 10)]
dp[0][0] = True
for i in range(N):
    for j in range(S + 1):
        if j >= A[i] and dp[i][j - A[i]]:
            dp[i + 1][j] = True
        if j >= B[i] and dp[i][j - B[i]]:
            dp[i + 1][j] = True

if not dp[N][S]:
    print("Impossible")
else:
    ans = ["?"] * N
    pos = S
    for i in range(N - 1, -1, -1):
        if pos >= B[i] and dp[i][pos - B[i]]:
            ans[i] = "B"
            pos -= B[i]
        else:
            ans[i] = "A"
            pos -= A[i]

    print("".join(ans))
