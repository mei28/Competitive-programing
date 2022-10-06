n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# iまでの最大値
A_max = [A[0]] * n

for i in range(1, n):
    A_max[i] = max(A[i], A_max[i - 1])

C = [0] * n

now_max = 0
for j in range(n):
    C[j] = max(A_max[j] * B[j], now_max)
    now_max = C[j]

for c in C:
    print(c)
