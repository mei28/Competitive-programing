N, M = map(int, input().split())
edges = [[] for _ in range(N)]
connected = [
    False
] * N  # 各頂点が少なくとも1つの辺に接続しているかを確認するためのフラグ

for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1  # 頂点番号を0-basedで扱う
    edges[u].append((v, w))
    connected[u] = connected[v] = True

# ウォークの存在判定
if not all(connected):
    print("No")

# DPテーブルの初期化
INF = float("inf")
dp = [[INF] * N for _ in range(1 << N)]

# 開始点のコストを0に設定
for i in range(N):
    dp[1 << i][i] = 0

# 遷移
for S in range(1 << N):
    for v in range(N):
        if dp[S][v] == INF:
            continue
        for u, w in edges[v]:
            if S & (1 << u) == 0:  # uが訪れた頂点集合に含まれない場合
                dp[S | (1 << u)][u] = min(dp[S | (1 << u)][u], dp[S][v] + w)

# 答えの計算
min_cost = min(dp[(1 << N) - 1])
print(min_cost if min_cost != INF else "No")
