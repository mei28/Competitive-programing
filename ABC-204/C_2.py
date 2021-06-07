N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

# dp[v] 頂点sからvに到達可能か?
dp = [False] * (N + 1)
