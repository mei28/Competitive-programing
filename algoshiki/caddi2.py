n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = A[:k][::-1]
C = []
for i in range(k):
    C.append(A[i + k] + B[i])
for j in range(2 * k, n):
    C.append(A[j])
print(min(C))
