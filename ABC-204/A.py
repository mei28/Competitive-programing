x, y = map(int, input().split())

if x != y:
    if 0 not in (x, y):
        print(0)
    elif 1 not in (x, y):
        print(1)
    else:
        print(2)
else:
    print(x)
