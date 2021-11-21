s, t, x = map(int, input().split())

if s < t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")

else:
    if s <= x:
        print("Yes")
        exit()
    t += 24
    x += 24

    if s <= x < t:
        print("Yes")
    else:
        print("No")
