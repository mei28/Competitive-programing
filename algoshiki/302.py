n, x, y = map(int, input().split())
A = [0] * (n + 10)
A[0] = x
A[1] = y

for i in range(2, n + 1):
    A[i] = (A[i - 2] + A[i - 1]) % 100

print(A[n - 1])
