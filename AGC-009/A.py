N = int(input())
A, B = [], []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    A[i] += C[i + 1]
    amari = A[i] % B[i]
    need = 0
    if amari != 0:
        need = B[i] - amari
    C[i] = C[i + 1] + need

print(C[0])
