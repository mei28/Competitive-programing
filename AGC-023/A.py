from collections import Counter

n = int(input())
A = list(map(int, input().split()))

S = [0] * (n + 1)

for i in range(n):
    S[i + 1] = S[i] + A[i]

cnter = Counter(S)

ans = 0

for k, v in cnter.items():
    ans += v * (v - 1) // 2

print(ans)
