from collections import deque

n = int(input())
A = list(map(int, input().split()))
A.sort()
Q = deque()
for a in A:
    Q.append(a)
cnt = 0
while len(Q) > 1:
    mi = Q.popleft()
    ma = Q.pop()

    tmp = ma % mi
    cnt += 1
    if tmp == 0:
        Q.appendleft(mi)
    elif tmp < mi:
        Q.appendleft(mi)
        Q.appendleft(tmp)
    else:
        Q.appendleft(tmp)
        Q.appendleft(mi)
print(cnt)
