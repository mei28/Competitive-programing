n = int(input())
A = list(map(int, input().split()))
A.reverse()
S = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + A[i]

ans = 0
for s in S:
    if s > 3:
        ans += 1

print(ans)
