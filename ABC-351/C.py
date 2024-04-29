from collections import deque
from typing import Deque

n = int(input())
A = list(map(int, input().split()))

B: Deque[int] = deque()

for a in A:
    B.append(a)

    while True:
        if len(B) == 1:
            break
        else:
            if B[-1] == B[-2]:
                tmp = B.pop()
                tmp = B.pop()
                tmp += 1
                B.append(tmp)
            else:
                break
print(len(B))
