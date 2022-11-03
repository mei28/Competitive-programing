a, b = map(int, input().split())


def f(x):
    if x % 4 == 0:
        return x
    if x % 4 == 1:
        return 1
    if x % 4 == 2:
        return 1 ^ x
    if x % 4 == 3:
        return 0


print(f(b) ^ f(a - 1))
