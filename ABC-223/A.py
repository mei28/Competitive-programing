x = int(input())

if x >= 100:
    if x != (x - x % 100):
        print("No")
        exit()
    else:
        print("Yes")
        exit()
else:
    print("No")
