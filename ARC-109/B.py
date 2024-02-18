n = int(input())

ok = 0
ng = n + 1

while ng - ok > 1:
    m = (ok + ng) // 2
    tmp_mid_sum = (m + 1) * m // 2

    if tmp_mid_sum <= n + 1:
        ok = m
    else:
        ng = m

print(n - ok + 1)
