from collections import deque
from os import wait

S = input()
que = deque()
que.append(set())

for s in S:
    if s == "(":
        old_set = que.pop()
        new_set = old_set.copy()
        que.append(old_set)
        que.append(new_set)
    elif s == ")":
        _ = que.pop()
    else:
        _set = que.pop()
        if s in _set:
            print("No")
            exit()
        else:
            _set.add(s)
            que.append(_set)
print("Yes")
