from bisect import bisect_left, bisect_right

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = -1
for a in A:
    idx = bisect_left(B, a)
    for i in range(-2, 2):
        if 0 <= i + idx < M:
            if abs(a - B[i + idx]) <= D:
                ans = max(ans, a + B[i + idx])

for b in B:
    idx = bisect_left(A, b)
    for i in range(-2, 2):
        if 0 <= i + idx < N:
            if abs(b - A[i + idx]) <= D:
                ans = max(ans, b + A[i + idx])
print(ans)
