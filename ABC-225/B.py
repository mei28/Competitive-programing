n = int(input())
edge = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)


e1 = 0
e2 = 0
for e in edge:
    if len(e) == 1:
        e1 += 1
    elif len(e) == n - 1:
        e2 += 1
    else:
        print("No")
        exit()
if e2 == 1 and e1 == n - 1:
    print("Yes")
else:
    print("No")
