b, c = map(int, input().split())

if c > 1:
    # [x-k,x+k]
    l1 = b - c // 2
    r1 = b + (c - 2) // 2
    # [-x+k,-x-k]
    l2 = -b - (c - 1) // 2
    r2 = -b + (c - 1) // 2

    if r2 < l1 or r1 < l2:
        ans = (r1 - l1 + 1) + (r2 - l2 + 1)
    else:
        ans = max(r1, r2) - min(l1, l2) + 1

else:
    if b == 0:
        ans = 1
    else:
        ans = 2

print(ans)
