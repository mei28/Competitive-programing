from collections import deque

n, k = map(int, input().split())
C = list(map(int, input().split()))

que = deque()

for i in range(k):
    que.append(C[i])

ans = len(set(que))

for i in range(k, n):
    que.popleft()
    que.append(C[i])
    ans = max(len(set(que)), ans)

print(ans)
