import heapq

n, m = map(int, input().split())
A = list(map(int, input().split()))

A = list(map(lambda x: -1 * x, A))
heapq.heapify(A)

for i in range(m):
    tmp_min = heapq.heappop(A)
    heapq.heappush(A, (-1) * (-tmp_min // 2))

print(-sum(A))
