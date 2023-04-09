a, b = map(int, input().split())
# b ちかづく
# a ちかづく
if a < b:
    a, b = b, a

diff = a - b

# A0 = 0
# A1 = b
# A2 = b + a
# A3 = b + a + b
# A4 = b + a + b + a
# A5 = b + a + b + a + b

# An = b + (n-1)/2*(a+b)
# An = n//2*(a+b)

# a,b
# a-b,b

ng = -1
ok = 10**18


def f(m):
    if m % 2 == 0:
        return b + (m - 1) // 2 * (a + b)
    else:
        return (a + b) * m // 2


while ok - ng > 1:
    mid = (ok + ng) // 2
    if diff <= f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
