n = int(input())

A = list(map(int, input().split()))

S = [0] * (n + 1)

for i in range(n):
    S[i + 1] = A[i] + S[i]

ans = 0
_max = -1

for i in range(n):
    _max = max(_max, A[i])
    ans += S[i + 1]
    print(ans + _max * (i + 1))
