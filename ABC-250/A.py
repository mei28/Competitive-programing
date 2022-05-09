h, w = map(int, input().split())
r, c = map(int, input().split())

if h == 1 and w == 1:
    print(0)
    exit()

elif h == 1:
    if c == 1 or w == c:
        print(1)
    else:
        print(2)
    exit()

elif w == 1:
    if r == 1 or h == r:
        print(1)
    else:
        print(2)
    exit()
else:
    if ((r == 1) or (h == r)) and ((c == 1) or (w == c)):
        print(2)
        exit()
    elif r == 1 or h == r:
        print(3)
        exit()
    elif c == 1 or w == c:
        print(3)
        exit()
    else:
        print(4)
