n, m = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]


B = []
for i in range(n + m):
    # print(A)
    # print(B)
    # print(C)
    # print('_'*20)
    # C
    for j in range(n):
        # A
        if A[j] == 0:
            continue
        s = C[i + j] // A[j]
        B.append(s)
        C[i] = 0
        for k in range(j + 1, n + 1):
            C[i + k] -= A[k] * s


print(*B[::-1])
