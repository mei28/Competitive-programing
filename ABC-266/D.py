n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]
G = list(sorted(G, key=lambda x: x[0]))

now = 0
