N = int(input())
A = list(map(int, input().split()))

S = [0] * (N + 1)

for i in range(0, N):
    S[i + 1] = S[i] + A[i]


diff = 1e20
for i in range(1, N):
    y = S[N] - S[i]
    x = S[i] - S[0]

    diff = min(diff, abs(x - y))

print(diff)
