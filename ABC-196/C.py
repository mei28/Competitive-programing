N = input()

cnt = 0
i = 1

while True:
    tmp = str(i) + str(i)
    if int(tmp) <= int(N):
        cnt += 1
    else:
        break
    i += 1
print(cnt)
