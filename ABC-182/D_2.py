n = int(input())
A = list(map(int, input().split()))
S = [0] * (n + 1)
M = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + A[i]
    M[i + 1] = max(M[i], S[i + 1])

res = 0
cur = 0

for i in range(n):
    res = max(res, cur + M[i + 1])
    cur += S[i + 1]

print(res)
