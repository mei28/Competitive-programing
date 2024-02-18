from itertools import combinations

N = int(input())

# N x N の2次元配列として D を初期化
D = [[0] * N for _ in range(N)]

# 入力を取得
for i in range(N - 1):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        D[i][i + j + 1] = val
        D[i + j + 1][i] = val

# すべての頂点の組み合わせでの最大値を計算
max_val = 0
for comb in combinations(range(N), N - 1 if N % 2 == 1 else N):
    dp = [-1] * (1 << len(comb))
    dp[0] = 0

    for S in range(1 << len(comb)):
        for i in range(len(comb)):
            for j in range(i + 1, len(comb)):
                if (S & (1 << i) == 0) and (S & (1 << j) == 0):
                    next_state = S | (1 << i) | (1 << j)
                    dp[next_state] = max(dp[next_state], dp[S] + D[comb[i]][comb[j]])

    max_val = max(max_val, dp[(1 << len(comb)) - 1])

print(max_val)
