x = int(input())

a = 360
while True:
    if a%x ==0:
        print(a//x)
        break
    else:
        a += 360

