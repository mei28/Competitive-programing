N, K = map(int, input().split())
L = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    L.append([a, b])

L = sorted(L, key=lambda x: x[0])

cnt = 0
for i in range(N):
    a, b = L[i]
    cnt += b
    if cnt >= K:
        print(a)
        exit()
