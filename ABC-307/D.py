from collections import deque

n = int(input())
S = input()

Q = deque()

cnt = 0
for s in S:
    if s == ")":
        if cnt == 0:
            Q.append(s)
            continue
        while cnt > 0:
            tmp = Q.pop()
            if tmp == "(":
                cnt -= 1
                break
    else:
        if s == "(":
            cnt += 1
        Q.append(s)

print("".join(Q))
