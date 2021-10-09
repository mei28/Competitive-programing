mod = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = 3000
dp = [1] * (M + 1)
for i in range(N):
    nx = [0] * (M + 1)
    for j in range(A[i], B[i] + 1):
        nx[j] = dp[j]
    dp = nx
    for i in range(M):
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
print(dp[M])


"""
ナイーブなDPを考える
dp[i][j]:= i番目までの要素が確定して，c_i=jである数
a_i <= j <= b_i のとき: 1つ前の要素以上であればok, それ以外はだめ

dp[i][j] = - 1 (i=0 and j=0)
           - dp[i-1][k] (1<=i and a<j<b)
           - 0 (else)
"""
