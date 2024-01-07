from collections import deque

n, q = map(int, input().split())

direction = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

history = deque()

for i in range(n, 0, -1):
    history.append((i, 0))

while q > 0:
    q -= 1
    a, b = input().split()
    if a == "1":
        po = history.pop()
        history.append(po)
        history.append((po[0] + direction[b][0], po[1] + direction[b][1]))
    else:
        print(*history[-int(b)])
