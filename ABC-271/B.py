n, q = map(int, input().split())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l[1:])

for _ in range(q):
    s, t = map(int, input().split())
    print(L[s - 1][t - 1])
