S = input()

cnt = 0
ans = 0
for s in S:
    if s == "W":
        ans += cnt
    else:
        cnt += 1

print(ans)
