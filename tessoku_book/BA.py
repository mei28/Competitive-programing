import heapq

q = int(input())

que = []
heapq.heapify(que)

for _ in range(q):
    l = input().split()
    if l[0] == "1":
        x = int(l[1])
        heapq.heappush(que, x)
    if l[0] == "2":
        print(que[0])
    if l[0] == "3":
        heapq.heappop(que)
