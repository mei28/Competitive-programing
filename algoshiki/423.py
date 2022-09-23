import sys

sys.setrecursionlimit(10**7)
n = int(input())
F = [-1] * (n + 10)


def fib(a):
    if F[a] != -1:
        return F[a]
    else:
        if a == 0:
            F[a] = 0
        elif a == 1:
            F[a] = 1
        else:
            F[a] = fib(a - 2) + fib(a - 1)
        return F[a]


print(fib(n))
