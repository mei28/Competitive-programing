n, m = map(int, input().split())

A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [0] * (m + 1)

for i in range(m, -1, -1):
    B[i] = C[i + n] // A[n]
    for j in range(n + 1):
        C[i + j] -= B[i] * A[j]

print(*B)
