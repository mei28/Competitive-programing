n, m = map(int, input().split())
parents = [-1] * n


def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if parents[x] > parents[y]:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x

    return True


def size(x):
    return -parents[find(x)]


# find cycle
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)
    if not union(u, v):
        print("No")
        exit()
flg = all([len(g) <= 2 for g in G])
if m == n - 1 and flg:
    print("Yes")
else:
    print("No")
