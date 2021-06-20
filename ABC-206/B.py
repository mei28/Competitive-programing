n = int(input())

i = 0
while True:
    tmp = i * (i + 1) // 2
    if tmp >= n:
        print(i)
        exit()
    i += 1
