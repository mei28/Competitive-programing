import sys

sys.setrecursionlimit(99999)

n, x, y = map(int, input().split())


A = [0] * (n + 1)
B = [0] * (n + 1)
A[n] = 1

for i in range(n, 1, -1):
    B[i] += A[i] * x
    A[i - 1] += A[i] + B[i]
    B[i - 1] += B[i] * y

print(B[1])
