A, B = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

# dp[i][j]: 左の山の一番上がa_i
#           右の山の一番上がb_j
#           のときの今から操作するプレイヤーの最適スコア
# dp[0][0] が一番最初の時

dp = [[0] * 1100 for _ in range(1100)]
a_sum = [0] * 1100
b_sum = [0] * 1100

for i in range(len(As) - 1, -1, -1):
    a_sum[i] = a_sum[i + 1] + As[i]
for i in range(len(Bs) - 1, -1, -1):
    b_sum[i] = b_sum[i + 1] + Bs[i]


for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B:
            dp[i][j] = 0
        elif i == A:
            dp[i][j] = b_sum[j] - dp[i][j + 1]
        elif j == B:
            dp[i][j] = a_sum[i] - dp[i + 1][j]
        else:
            dp[i][j] = a_sum[i] + b_sum[j] - min(dp[i + 1][j], dp[i][j + 1])

print(dp[0][0])
