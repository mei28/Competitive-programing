n = 400
m = 1995

Ps = []
Xs = []
Ys = []

for _ in range(n):
    x, y = map(int, input().split())
    Xs.append(x)
    Ys.append(y)
    Ps.append([x, y])

Us, Vs, UVs = [], [], []
for i in range(m):
    u, v = map(int, input().split())
    Us.append(u)
    Vs.append(v)
    UVs.append([u, v])

for i in range(m):
    l = int(input())
    print(1, end=" ", flush=True)
