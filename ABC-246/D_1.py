n = int(input())

def f(a,b):
    return a**3 + (a**2)*b + (b**2)*a + b**3

ans = -1

for a in range(10**6):
    ng = -1
    ok = 10**6

    while ng+1 != ok:
        mid = (ng+ok)//2
        if n<=f(a,mid):
            ok = mid
        else:
            ng = mid
    if ans ==-1:
        ans = f(a,ok)
    ans = min(ans,f(a,ok))

print(ans)
