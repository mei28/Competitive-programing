n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False, False] for _ in range(n + 2)]
dp[0] = [True, True]

for i in range(n - 1):
    for j in range(2):
        if dp[i][j]:
            if j == 0:
                a = A[i]
            else:
                a = B[i]
            if abs(a - A[i + 1]) <= k:
                dp[i + 1][0] = True
            if abs(a - B[i + 1]) <= k:
                dp[i + 1][1] = True


# print(dp)
if dp[n - 1][0] or dp[n - 1][1]:
    print("Yes")
else:
    print("No")
