n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)


p = [-1] * (n)

def root(x:int)->int:
    if p[x]<0:
        return x
    p[x] = root(p[x])
    return p[x]

def merge(x:int,y:int):
    x = root(x)
    y = root(y)
    if x==y:
        return 
    if x>y:
        x,y = y,x
    p[x] += p[y]
    p[y] = x


for a in range(n):
    for b in G[a]:
        merge(a,b)
ans = 0

for i in range(n):
    if i==root(i):
        ans += 1

print(ans-1)
