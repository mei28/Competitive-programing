import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

k = int(input())


@lru_cache
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


ng = 0
ok = k + 1

while ok - ng > 1:
    mid = (ng + ok) // 2
    fac = fact(mid)

    if fac % k == 0:
        ok = mid
    else:
        ng = mid
print(ok)
