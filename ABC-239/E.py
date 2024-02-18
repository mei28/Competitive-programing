n, q = map(int, input().split())

X = [0] + list(map(int, input().split()))


edge = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


Q = list()
# [今いる時点，今いる頂点の親，訪問回数]
Q.append([1, 0, 1])
# 部分木の頂点に書いてある数をソートしたもの
P = [[0]]

for i in range(1, n + 1):
    P.append([X[i]])

while len(Q) > 0:
    now, parent, count = Q.pop()

    if count == 1:
        Q.append([now, parent, count + 1])

        for to in edge[now]:
            if to != parent:
                Q.append([to, now, count])
    else:
        for to in edge[now]:
            if to == parent:
                continue

            P[now] += P[to]
            P[now].sort(reverse=True)

            P[now] = P[now][:20]

for i in range(q):
    v, k = map(int, input().split())
    k -= 1
    print(P[v][k])
