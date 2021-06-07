n = int(input())
T = list(map(int, input().split()))

all_sum = sum(T)

dp = [False] * (all_sum + 1)

dp[0] = True

for t in T:
    for i in range(all_sum, t - 1, -1):
        dp[i] |= dp[i - t]

ans = all_sum // 2
if all_sum % 2 == 1:
    ans += 1

while dp[ans] == False:
    ans += 1

print(ans)
