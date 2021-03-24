from collections import deque

s = deque(input())
q = int(input())

flip = 1

for i in range(q):
    line = list(input().split())

    if line[0] == "1":
        flip = 1 - flip
    else:
        f, c = line[1], line[2]

        if flip:
            if f == "1":
                s.appendleft(c)
            else:
                s.append(c)
        else:
            if f == "1":
                s.append(c)
            else:
                s.appendleft(c)

if flip:
    print("".join(s))
else:
    s.reverse()
    print("".join(s))
