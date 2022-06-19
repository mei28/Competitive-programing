h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
ma = 30
for a in range(1, ma):
    for b in range(1, ma):
        c = h1 - a - b
        if c < 1:
            break
        for d in range(1, ma):
            for e in range(1, ma):
                f = h2 - d - e
                if f < 1:
                    break
                for g in range(1, ma):
                    for h in range(1, ma):
                        i = h3 - g - h
                        if i < 1:
                            break

                        flg1 = True if a + d + g == w1 else False
                        flg2 = True if b + e + h == w2 else False
                        flg3 = True if c + f + i == w3 else False

                        if flg1 and flg2 and flg3 and True:
                            ans += 1
                            # print("-" * 30)
                            # print(a, b, c)
                            # print(d, e, f)
                            # print(g, h, i)

print(ans)
