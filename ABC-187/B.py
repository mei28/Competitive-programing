N = int(input())
D = []
for i in range(N):
    line = list(map(int, input().split()))
    D.append(line)
cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        a = D[i]
        b = D[j]

        if abs((a[1] - b[1]) / (a[0] - b[0])) <= 1:
            cnt += 1

print(cnt)
