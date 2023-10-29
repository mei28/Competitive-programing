n = int(input())

for abc in range(n, 10**8 - 1):
    a = int(str(abc)[0])
    b = int(str(abc)[1])
    c = int(str(abc)[2])

    if a * b == c:
        print(abc)
        exit()
