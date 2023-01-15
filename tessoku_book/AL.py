D, N = map(int, input().split())
constraint = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for d in range(1, D + 1):
    work = 24
    for l, r, h in constraint:
        if l <= d <= r:
            work = min(work, h)

    ans += work

print(ans)
