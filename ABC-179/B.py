n = int(input())

D = []
for i in range(n):
    d = list(map(int, input().split()))
    D.append(d)

flg = False
cnt = 0

for i in D:
    a, b = i[0], i[1]
    if a == b:
        cnt += 1

    else:
        cnt = 0

    if cnt >= 3:
        flg = True
        break
if flg:
    print('Yes')
else:
    print('No')
