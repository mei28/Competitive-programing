import math
from itertools import combinations
L = int(input())


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


base = comb(L-1, 11)
print(base)  # 10
