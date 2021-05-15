S = input()
ans = 0
for i in range(10000):
    T = "%04d" % (i)
    ok = True

    for d in range(10):
        if S[d] == "?":
            continue
        if S[d] == "o":
            if str(d) not in T:
                ok = False
        if S[d] == "x":
            if str(d) in T:
                ok = False

    if ok:
        ans += 1

print(ans)
