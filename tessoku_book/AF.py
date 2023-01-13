n, a, b = map(int, input().split())
# dp[i]: 山がiのときにfirstがかつ
dp = [True] * (n + 1)

dp[0] = False

for i in range(a):
    dp[i] = False

for i in range(a, n + 1):
    dp[i] = False
    for j in [a, b]:
        nxt = i - j
        if nxt < 0:
            continue
        if not dp[nxt]:
            dp[i] = True
print("First" if dp[n] else "Second")
