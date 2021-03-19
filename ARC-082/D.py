N = int(input())
P = list(map(int, input().split()))
i = 0

cnt = 0
for i in range(len(P)):
    if P[i] == i + 1:
        if P[i] == N:
            P[i - 1], P[i] = P[i], P[i - 1]
        else:
            P[i], P[i + 1] = P[i + 1], P[i]

        cnt += 1
print(cnt)
