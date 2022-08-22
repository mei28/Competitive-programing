n, p, q, r = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + A[i]

S = set(S)
T = list(S)

for s in S:
    if s + p in S and s + p + q in S and s + p + q + r in S:
        print("Yes")
        exit()
print("No")
