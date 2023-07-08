import math


def c(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def f(n, k):
    left = c(n + 2, k + 1)
    right = c(n, k - 1) + c(n, k + 1)
    return left == right * 2


for n in range(2, 20 + 1):
    for k in range(1, n):
        if f(n, k):
            print("n = ", n, " k = ", k, " f(n, k) = ", f(n, k))
