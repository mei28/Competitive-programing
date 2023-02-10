n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [[0] * (n + 1) for _ in range(k)]

for j in range(k):
    for i in range(n):
        S[j][i + 1] = S[j][i] + (A[j] if i % k == j else 0)

q = int(input())
