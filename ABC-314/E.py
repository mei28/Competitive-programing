N, M = map(int, input().strip().split())
roulettes = [tuple(map(int, input().strip().split())) for _ in range(N)]

# dp[i]はポイントiに達するための最小のコスト
dp = [float('inf')] * (M + 1)
dp[M] = 0

# ポイントMから0まで計算
for i in range(M, -1, -1):
    for cost, P, *points in roulettes:
        # 現在のポイントからの遷移を計算
        expected_cost = 0
        for point in points:
            next_point = min(M, i + point)
            # 各ポイントに遷移する確率は1/P
            expected_cost += dp[next_point] / P
        # 現在のポイントに遷移するコストとして記録
        dp[i] = min(dp[i], cost + expected_cost)

print(dp[0])
