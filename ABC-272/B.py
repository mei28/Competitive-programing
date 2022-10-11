n, m = map(int, input().split())
G = [set() for _ in range(n + 1)]

for _ in range(m):
    l = list(map(int, input().split()))
    k = l[0]
    l = l[1:]

    for i in range(k):
        for j in range(k):
            G[l[i]].add(l[j])
G = G[1:]

flg = all([len(a) == n for a in G])
print("Yes") if flg else print("No")
