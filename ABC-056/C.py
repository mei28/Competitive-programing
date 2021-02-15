X = int(input())

i = 0
cnt = 0
while cnt < X:
    i += 1
    cnt = (1 + i) * i // 2
print(i)
