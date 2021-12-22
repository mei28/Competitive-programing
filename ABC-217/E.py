from collections import deque
import heapq
n = int(input())

que = deque()
hq = []

for i in range(n):
    query = input()
    if query[0]=="1":
        q,x = query.split()
        que.append(int(x))
    elif query[0]=="2":
        if len(hq) > 0:
            print(heapq.heappop(hq))
        else:
            print(que.popleft())
    else:
        while que:
            heapq.heappush(hq,que.pop())
