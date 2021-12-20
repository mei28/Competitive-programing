m = int(input())
edge = [[] for _ in range(9)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    edge[u].append(v)
    edge[v].append(u)

P = list(map(lambda x: int(x) - 1, input().split()))
used = [True] * 9
for place in P:
    used[place] = False
empty = 0
while not used[empty]:
    empty += 1
P.append(empty)

goal = 123456789

dist = {P: 0}
vec = [P]

while len(vec)!=0:
    new_vec = []
    for 
