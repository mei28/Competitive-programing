n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
x = int(input())

dp = [False] * (x + 1)
dp[0] = True


for j in range(x + 1):
    if j in B:
        dp[j] = False
        continue

    for i in range(n):
        a = A[i]
        if j - a >= 0:
            dp[j] |= dp[j - a]

print("Yes" if dp[x] else "No")
