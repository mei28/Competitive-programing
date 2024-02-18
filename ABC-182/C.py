N = input()

sum_ = 0
ans = 0
dic = {"0": 0, "1": 0, "2": 0}
for i in N:
    sum_ += int(i)
    idx = str(int(i) % 3)
    dic[idx] = dic[idx] + 1


cnt = 0

for k, v in dic.items():
    cnt += v

if sum_ % 3 == 1:
    if dic["1"] > 0:
        if cnt > 1:
            print(1)
        else:
            print(-1)
        exit()
    elif dic["2"] > 0:
        if cnt > 2:
            print(2)
        else:
            print(-1)
        exit()
    else:
        print(-1)
        exit()

if sum_ % 3 == 2:
    if dic["2"] > 0:
        if cnt > 1:
            print(1)
        else:
            print(-1)
        exit()
    elif dic["1"] > 1:
        if cnt > 2:
            print(2)
        else:
            print(-1)
        exit()
    else:
        print(-1)
if sum_ % 3 == 0:
    print(ans)
    exit()
