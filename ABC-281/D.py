n, k, d = map(int, input().split())
A = list(map(int, input().split()))

MAX_N = 102
MAX_M = 102
INF = float("inf")
dp0 = [[INF] * MAX_M for _ in range(MAX_N)]
dp1 = [[INF] * MAX_M for _ in range(MAX_N)]

sum_A = sum(A)

# init
for j in range(k, n + 1):
    for s in range(sum_A + 1):
        dp0[j][s] = INF
        dp1[j][s] = INF
