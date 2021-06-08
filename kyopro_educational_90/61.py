from collections import deque

q = int(input())

T = []
dq = deque()
for _ in range(q):
    t, x = map(int, input().split())
    T.append([t, x])


for t, x in T:
    if t == 1:
        dq.appendleft(x)
    elif t == 2:
        dq.append(x)
    else:
        print(dq[x - 1])
