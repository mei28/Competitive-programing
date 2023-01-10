from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
INF = float("inf")
dp = [INF] * (n + 2)
# dp[i]: 長さがiの最小値

for a in A:
    idx = bisect_left(dp, a)
    dp[idx] = a
ans = 0
while dp[ans] != INF:
    ans += 1

print(ans)
