n, q = map(int, input().split())
A = [i + 1 for i in range(n)]
for _ in range(q):
    s = int(input())

    idx = A.index(s)
    right_idx = idx + 1
    if right_idx >= n:
        right_idx = idx - 1

    A[idx], A[right_idx] = A[right_idx], A[idx]
print(*A)
