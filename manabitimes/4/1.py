# encoding: utf-8
import sys

sys.setrecursionlimit(90000)
all_ = []
cnt = 0


def check(num: int):
    if num % 3 == 0:
        return 1
    return 0


def dfs(A: list, n: int):
    if len(A) == n:
        tmp = int("".join(A))
        return check(tmp)

    cnt = 0
    for v in [1, 2]:
        A.append(str(v))
        cnt += dfs(A, n)
        A.pop()
    return cnt


if __name__ == "__main__":
    for n in range(1, 10):
        print(n, dfs([], n), 2**n)

    pass
