n,m = map(int,input().split())
H = list(map(int,input().split()))
edge = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    edge[a].append(b)
    edge[b].append(a)


ans = 0
for i in range(n):
    ok:bool = True
    for to in edge[i]:
        if H[i] <= H[to]:
            ok=False
            break
    if ok:
        ans += 1
        

print(ans)
