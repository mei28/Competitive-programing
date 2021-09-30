import sys
from typing import List

sys.setrecursionlimit(5000)

k = int(input())

all_: List[int] = []


def dfs(d: int, val: int, all_: List[int]) -> None:
    all_.append(val)
    if d == 10:
        return

    for j in [-1, 0, 1]:
        add = (val % 10) + j
        if add >= 0 and add <= 9:
            dfs(d + 1, val * 10 + add, all_)


for i in range(1, 10):
    dfs(1, i, all_)

all_.sort()
print(all_[k - 1])
