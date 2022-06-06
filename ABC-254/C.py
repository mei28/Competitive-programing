n, k = map(int, input().split())
A = list(map(int, input().split()))

B = [[] for _ in range(k)]
for i, x in enumerate(A):
    B[i % k].append(x)

for i in range(k):
    B[i].sort()

SA = [0] * n
for i in range(n):
    SA[i] = B[i % k][i // k]

print("Yes") if sorted(A) == SA else print("No")
