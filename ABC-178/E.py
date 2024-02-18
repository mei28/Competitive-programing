n = int(input())

P = [tuple(map(int, input().split())) for _ in range(n)]

P.sort()

WZ = [(x + y, x - y) for x, y in P]
W = [x + y for x, y in P]
Z = [x - y for x, y in P]

print(max(max(W) - min(W), max(Z) - min(Z)))
