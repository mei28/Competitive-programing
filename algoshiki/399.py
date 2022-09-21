import enum

n = int(input())
W = list(map(int, input().split()))
D = [[w, i] for i, w in enumerate(W)]
D.sort()

E = [[w, i, j] for j, (w, i) in enumerate(D)]
E = list(sorted(E, key=lambda x: x[1]))
for e in E:
    print(e[2])
