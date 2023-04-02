# 入力を受け取る
N, A = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

S = [P, Q, R]

# DP テーブルと初期化に使う大きな数
INF = 1 << 30
dp = [[INF for _ in range(3)] for _ in range(N)]

# DP 初期条件
for s in range(3):
    dp[0][s] = S[s][0]

# DP テーブルの更新
for i in range(1, N):
    for s in range(3):
        # dp[i][s] を求める
        cost = INF
        for ps in range(3):
            # 前日に選んだ店 ps で場合分けをして、価格の総和の最小値を更新する
            if ps == s:
                cost = min(cost, dp[i - 1][ps] + S[s][i] - A)
            else:
                cost = min(cost, dp[i - 1][ps] + S[s][i])
        dp[i][s] = cost

# 答えを出力する
ans = INF
for s in range(3):
    ans = min(ans, dp[N - 1][s])
print(ans)
