from collections import Counter

n = int(input())


def fact(a: int) -> list:
    ret = []

    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            while a % i == 0:
                ret.append(i)
                a //= i

    if a != 1:
        ret.append(a)
    return ret


factor = fact(n)
cnter = Counter(factor)

ans = 0
for k, v in cnter.items():
    tmp = 0
    cur = 1
    while v >= cur:
        v -= cur
        cur += 1
        tmp += 1
    ans += tmp

print(ans)
