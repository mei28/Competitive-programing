n, t = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

set_C = set(C)

if t not in C:
    ans = -1
    ans_max = -1
    t = C[0]
    for i in range(n):
        c, r = C[i], R[i]
        if c == t:
            if ans_max < r:
                ans_max = r
                ans = i + 1
    print(ans)
    pass
else:
    ans = -1
    ans_max = -1
    for i in range(n):
        c, r = C[i], R[i]
        if c == t:
            if ans_max < r:
                ans_max = r
                ans = i + 1
    print(ans)

    pass
