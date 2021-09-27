from collections import deque

x = input()

dq: deque = deque()

for s in x:
    if s == "T":
        if len(dq) == 0:
            dq.append(s)
        else:
            poped = dq.pop()
            if poped == "S":
                continue
            else:
                dq.append(poped)
                dq.append(s)
    else:
        dq.append("S")

print(len(dq))
