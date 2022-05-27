from heapq import heapify, heappop, heappush

n, k = map(int, input().split())
P = list(map(int, input().split()))
pq = P[:k]

heapify(pq)

print(pq[0])

for x in P[k:]:
    heappush(pq, x)
    heappop(pq)
    print(pq[0])
