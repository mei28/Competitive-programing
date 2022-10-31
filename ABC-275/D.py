from collections import defaultdict

n = int(input())
F = defaultdict(int)
F[0] = 1


def f(n):
    if n == 0:
        return 1
    if n in F.keys():
        return F[n]
    else:
        F[n] = f(n // 2) + f(n // 3)
        return F[n]


f(n)
print(F[n])
