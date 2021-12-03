N, K = map(int, input().split())
MOD = 10 ** 9 + 7

low, high = 0, 0
ans = 0
for x in range(1, N + 2):
    low += x - 1
    high += N - x + 1

    if x >= K:
        ans += (high - low + 1)
        ans %= MOD

print(ans)
