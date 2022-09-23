import sys

sys.setrecursionlimit(10**7)
a, b = map(int, input().split())


def f(x):
    if x == a:
        return a
    else:
        return x + f(x - 1)


print(f(b))
