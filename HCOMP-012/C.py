import heapq


n, m = map(int, input().split())
A = list(map(int, input().split()))
A = [-a for a in A]

heapq.heapify(A)

while m > 0:
    a = heapq.heappop(A)
    a = -(-a // 2)
    heapq.heappush(A, a)
    m -= 1

print(-sum(A))
