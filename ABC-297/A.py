n, d = map(int, input().split())
T = list(map(int, input().split()))

for i in range(1, n):
    a = T[i - 1]
    b = T[i]

    if b - a <= d:
        print(b)
        exit()
print(-1)
