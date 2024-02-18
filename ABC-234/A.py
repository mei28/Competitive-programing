t = int(input())


def f(t):
    return t * t + 2 * t + 3


print(f(f(f(t) + t) + f(f(t))))
