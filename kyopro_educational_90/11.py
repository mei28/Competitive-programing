N = int(input())

A = []

D, C, S = [], [], []
for i in range(N):
    d, c, s = map(int, input().split())
    A.append((d, c, s))
    D.append(d)
    C.append(c)
    S.append(s)
A = list(sorted(A, key=lambda x: x[0]))
# D日締め切り, C日間，S円報酬
ans = 0
for bit in range(1 << N):
    for j in range(N):
        tmp = 0
        days = 0
        print("-" * 20)
        if (bit >> j) % 2 == 1:
            print(A[j])
            if days < A[j][0]:
                days += A[j][1]
                tmp += A[j][2]
    ans = max(ans, tmp)

print(ans)
