a, b = map(int, input().split())

while a < b:
    if b % 2 == 0:
        b //= 2
    else:
        b = (b - 1) // 2

    if b == a:
        print("Yes")
        exit()
    break
print("No")
