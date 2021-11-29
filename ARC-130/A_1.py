n = int(input())
S = input()

from itertools import groupby


def rls(S: str):
    grouped = groupby(S)
    ans = 0
    for k, v in grouped:
        v = int(v)
        ans += v * (v - 1)
    ans //= 2
    return ans


print(rls(S))
