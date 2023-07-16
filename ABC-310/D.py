import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)


def dfs(v, c):
    group[v] = c
    for i in G[v]:
        if group[i] == c:
            return False
        if group[i] == 0 and not dfs(i, -c):
            return False
    return True


N, M, T = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
MOD = 10**9 + 7
G = defaultdict(list)
for a, b in edges:
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

group = [0] * N
nums = [0, 0]
for v in range(N):
    if group[v] == 0:
        if not dfs(v, 1):
            print(0)
            exit()
        c1 = sum(1 for i in range(N) if group[i] == 1)
        c2 = sum(1 for i in range(N) if group[i] == -1)
        nums.append(c1)
        nums.append(c2)

dp = [0] * (N + 1)
dp[0] = 1
for c in nums:
    dp_next = dp[:]
    for i in range(c, N + 1):
        dp_next[i] += dp[i - c]
        dp_next[i] %= MOD
    dp = dp_next

ans = 0
for i in range(T, N + 1):
    ans += dp[i]
    ans %= MOD
print(ans)
