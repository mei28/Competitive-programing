n, p, q, r, s = map(int, input().split())
p -= 1
r -= 1

A = list(map(int, input().split()))

B = A[:p] + A[r:s] + A[q:r] + A[p:q] + A[s:]
print(*B)
