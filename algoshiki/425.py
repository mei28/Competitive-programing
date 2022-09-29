n = int(input())


def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a - 2) + fib(a - 1)


print(fib(n))
