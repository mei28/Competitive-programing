import math

K = int(input())
R = [int(input()) for _ in range(1 << K)]

dp = [[0 for _ in range(11)] for _ in range((1 << K) + 100)]


def f(p, q):
    return 1 / (1 + math.pow(10, (R[q] - R[p]) / 400))


N = 1 << K

for i in range(N):
    # みんな0回戦は勝つ
    dp[i][0] = 1

for j in range(K):
    for i in range(N):
        # j桁より上を全て残す
        upper = i & ~((1 << j) - 1)
        # j桁目をひっくり返す
        upper ^= 1 << j
        for other in range(upper, upper + (1 << j), 1):
            # iがj+1回戦に上がる = iがjにいる*敵がjにいる*iが勝つ
            dp[i][j + 1] += dp[i][j] * dp[other][j] * f(i, other)


for i in range(N):
    print(dp[i][K])
