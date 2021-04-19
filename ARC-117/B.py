N = int(input())
A = list(map(int, input().split()))

A.sort()

MOD = 1000000007
Q = [A[0]]

for i in range(1, N):
    Q.append(A[i] - A[i - 1])

ans = 1
for q in Q:
    ans *= q + 1
    ans %= MOD

print(int(ans))
