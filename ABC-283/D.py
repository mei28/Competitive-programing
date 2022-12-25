import string
from collections import deque

S = input()

if S.count("(") != S.count(")"):
    print("No")
    exit()

q = deque()
q.append(set())
for s in S:
    # print(q)
    if s == "(":
        se = q.pop()
        q.append(se)
        q.append(se.copy())
    elif s in string.ascii_lowercase:
        se = q.pop()
        if s not in se:
            se.add(s)
            q.append(se)
        else:
            print("No")
            exit()
    elif s == ")":
        if len(q) > 0:
            q.pop()

print("Yes")
