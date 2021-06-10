n = int(input())
a = [i for i in range(1, n + 1)]
s = [0] * (n + 1)

for i in range(n):
    s[i + 1] = s[i] + a[i]


ng = 0
ok = n + 1


def is_ok(m):
    if s[m] >= n:
        return True
    return False


while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

i = s[ok] - n

for j in range(1, ok + 1):
    if j == i:
        continue
    print(j)
