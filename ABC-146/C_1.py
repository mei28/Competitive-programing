a, b, x = map(int, input().split())


def check(n):
    return a * n + b * len(str(n))

ok = -1 
ng = 10**9 + 1

while ng -ok >1:
    mid = (ok+ng)//2
    money = check(mid)
    if money <= x:
        ok = mid
    else:
        ng = mid

print(ok if ok >0 else 0)
