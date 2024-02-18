n, h, x = map(int, input().split())
P = list(map(int, input().split()))

for i in range(n):
    if P[i] + h >= x:
        print(i + 1)
        exit()
