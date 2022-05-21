n = int(input())
A = list(map(int, input().split()))

A.sort()

S = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + A[i]

MOD = 1000000007

ans = 0
for i in range(n - 1):
    ans += A[i] * (S[n] - S[i + 1])
    ans %= MOD

print(ans)
