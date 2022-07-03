n, x = map(int, input().split())
A = []
B = []
B_min = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    B_min.append(b)

for i in range(1, n):
    A[i] += A[i - 1]
    B[i] += B[i - 1]
    B_min[i] = min(B_min[i], B_min[i - 1])

ans = 10 ** 30
for i in range(n):
    tmp = A[i] + B[i] + B_min[i] * max(0, (x - (i + 1)))
    ans = min(ans, tmp)

print(ans)
