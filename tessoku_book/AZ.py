from collections import deque

q = int(input())
que = deque()

for _ in range(q):
    l = input().split()
    if l[0] == "1":
        x = l[1]
        que.append(x)
        pass
    if l[0] == "2":
        x = que.popleft()
        print(x)
        que.appendleft(x)
    if l[0] == "3":
        x = que.popleft()
