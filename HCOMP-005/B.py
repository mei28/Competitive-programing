from itertools import permutations

n, m = map(int, input().split())
G = [[False] * n for _ in range(n)]
T = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a][b] = True
    G[b][a] = True

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    T[a][b] = True
    T[b][a] = True


for P in permutations(range(n)):
    flg = True
    for i in range(n):
        for j in range(n):
            if G[i][j] != T[P[i]][P[j]]:
                flg = False

    if flg:
        print("Yes")
        exit()
print("No")
