s = input()

if len(s) <= 2:
    if(int(s) % 8 == 0 or int(s[::-1]) % 8 == 0):
        print("Yes")
    else:
        print("No")
    exit()

cnt = [0] * 10

for c in s:
    num = ord(c) - ord('0')
    cnt[num] += 1

for i in range(100, 1000):
    if i % 8 != 0:
        continue
    x = str(i)
    if '0' in x:
        continue
    tmp_cnt = [0] * 10
    for c in x:
        num = ord(c) - ord('0')
        tmp_cnt[num] += 1

    ok = True
    for d in range(10):
        if tmp_cnt[d] > cnt[d]:
            ok = False
    if ok:
        print("Yes")
        exit()

print("No")
