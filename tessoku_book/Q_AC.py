n = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0] * (n + 5)
# dp[i]: 部屋iに来るまでにかかる時間
# dp[i] = min(dp[i-1]+A_i,dp[i-2]+B_i,dp[i])

before = [0] * (n + 2)

for i in range(1, n):
    if i == 1:
        dp[i] = dp[i - 1] + A[i]
        before[i] = i - 1
    else:
        use_A = dp[i - 1] + A[i]
        use_B = dp[i - 2] + B[i]
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])
        if use_A <= use_B:
            before[i] = i - 1
        else:
            before[i] = i - 2

ans = [n]
now = n - 1
while now != 0:
    now = before[now]
    ans.append(now + 1)
ans = ans[::-1]

print(len(ans))
print(*ans)
