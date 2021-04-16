N = int(input())
C = [[0 for _ in range(N)] for _ in [0, 1]]
for i in range(N):
    c, p = map(int, input().split())
    if c == 2:
        C[1][i] = p
    else:
        C[0][i] = p

sum_C_0 = [0 for _ in range(N + 1)]
sum_C_1 = [0 for _ in range(N + 1)]

for i in range(1, N):
    sum_C_0[i + 1] = sum_C_0[i] + C[0][i]
    sum_C_1[i + 1] = sum_C_1[i] + C[1][i]


Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    print(sum_C_0[r] - sum_C_0[l], sum_C_1[r] - sum_C_1[l])
