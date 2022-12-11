h, m = map(int, input().split())

a, b, c, d = "0", "0", "0", "0"
if h < 10:
    a = "0"
    c = str(h)
else:
    a = str(h)[0]
    c = str(h)[1]
if m < 10:
    b = "0"
    d = str(m)
else:
    b = str(m)[0]
    d = str(m)[1]


def check(a, b, c, d):
    if a == "2" and int(b) >= 4:
        return False
    if int(b) >= 6:
        return False

    if int(c) < 6:
        return True
    if int(a + c) >= 24 or int(b + d) >= 60:
        return False

    else:
        return False


while True:
    if check(a, b, c, d):
        print(int(a + c), int(b + d))
        exit()
    bd = int(b + d) + 1
    ac = a + c
    if bd >= 60:
        b = str(0)
        d = str(0)

        ac = int(ac) + 1
        if ac >= 24:
            a = str(0)
            b = str(0)
            c = str(0)
            d = str(0)
            continue
        if ac < 10:
            a = str(0)
            c = str(ac)
        else:
            a = str(ac)[0]
            c = str(ac)[1]

    else:
        a = str(ac)[0]
        c = str(ac)[1]
        if bd >= 10:
            b = str(bd)[0]
            d = str(bd)[1]
        else:
            b = str(0)
            d = str(bd)
