from collections import deque
from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
outdeg = [[] for _ in range(n)]
indeg = [0] * (n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    indeg[b] += 1
    outdeg[a].append(b)

for i in range(n):
    heapify(outdeg[i])

que = []
heapify(que)
for i in range(n):
    if indeg[i] == 0:
        heappush(que, i)

ans = []

while len(que) > 0:
    t = heappop(que)
    ans.append(t + 1)
    tmp = [heappop(outdeg[t]) for _ in range(len(outdeg[t]))]
    for j in tmp:
        indeg[j] -= 1
        if indeg[j] == 0:
            heappush(que, j)
if len(ans) != n:
    print(-1)
else:
    print(*ans)
