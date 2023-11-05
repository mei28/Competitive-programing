import math

# 入力
N = int(input())
P = list(map(int, input().split()))

# DPテーブルの初期化 (-infで初期化して、選択されていないことを示す)
dp = [[-float("inf")] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0  # 0個のコンテストを選んだときのレートは0

# DPテーブルを更新する
for i in range(1, N + 1):  # 選んだコンテストの数
    for j in range(1, N + 1):  # 最後に選んだコンテストの位置
        # それまでの最大レートを求める
        for k in range(j):  # 前に選んだコンテストの位置
            if dp[i - 1][k] != -float("inf"):
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + P[j - 1] * (0.9 ** (i - 1)))

# 最大レートの探索
max_rate = -float("inf")
for k in range(1, N + 1):  # 選んだコンテストの数
    for i in range(1, N + 1):  # 最後に選んだコンテストの位置
        if dp[k][i] != -float("inf"):
            weight_sum = sum((0.9) ** (k - idx) for idx in range(k))
            rate = dp[k][i] / weight_sum - (1200 / math.sqrt(k))
            max_rate = max(max_rate, rate)


# 出力
print(max_rate)
