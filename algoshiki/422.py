import sys

sys.setrecursionlimit(10**7)
n = int(input())


def f(x):
    if x == 0:
        return 0
    else:
        return x + f(x - 1)


print(f(n))
