b = int(input())

for a in range(1, 99999999):
    if a**a == b:
        print(a)
        exit()
    if a**a > b:
        break
print(-1)
