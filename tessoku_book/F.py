n, q = map(int, input().split())

A = list(map(int, input().split()))

S = [0] * (n + 10)

for i in range(n):
    S[i + 1] = A[i] + S[i]
for _ in range(q):
    l, r = map(int, input().split())
    print(S[r] - S[l - 1])
