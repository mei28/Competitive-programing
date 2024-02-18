from collections import deque

a, n = map(int, input().split())

m = 1

while m <= n:
    m *= 10

d = [-1] * m

que = deque()
d[1] = 0
que.append(1)

while len(que):
    c = que.popleft()
    dc = d[c]

    op1 = a * c

    if op1 < m and d[op1] == -1:
        d[op1] = dc + 1
        que.append(op1)

    if c >= 10 and c % 10 != 0:
        s = str(c)
        op2 = int(s[-1] + s[:-1])
        if op2 < m and d[op2] == -1:
            d[op2] = dc + 1
            que.append(op2)

print(d[n])
