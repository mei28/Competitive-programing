x = int(input())

if 6 < x <= 11:
    print(2)
    exit()
if x <= 6:
    print(1)
    exit()


a = x // 11 * 2
b = x % 11
if b == 0:
    print(a)
elif b <= 6:
    print(a + 1)
else:
    print(a + 2)
