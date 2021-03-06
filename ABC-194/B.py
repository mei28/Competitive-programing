N = int(input())

A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10000000
for i in range(N):
    for j in range(N):
        if i == j:
            now = A[i] + B[j]
        else:
            now = max(A[i], B[j])
        ans = min(ans, now)

print(ans)
