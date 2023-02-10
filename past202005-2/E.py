n, m, q = map(int, input().split())


G = [[] for _ in range(n + 1)]


for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

colors = [0] + list(map(int, input().split()))


def q1(x):
    x = int(x)
    print(colors[x])
    c = colors[x]
    for nx in G[x]:
        colors[nx] = c


def q2(x, y):
    x, y = map(int, [x, y])
    print(colors[x])
    colors[x] = y


for _ in range(q):
    s = input()
    if s.split()[0] == "1":
        q1(s.split()[1])
    else:
        q2(s.split()[1], s.split()[2])
        pass
