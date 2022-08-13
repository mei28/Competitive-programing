r, c = map(int, input().split())

if r > c:
    r, c = c, r


if r == 1 or c == 1 or r == 15 or c == 15:
    print("black")
    exit()

if r % 2 == 0:
    if r <= c <= 15 - r + 1:
        print("white")
        exit()
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
        exit()
elif r % 2 == 1:
    if r <= c <= 15 - r + 1:
        print("black")
        exit()
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")
        exit()
