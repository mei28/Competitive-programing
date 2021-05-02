mat = []
N = 20

prime_list = []

for i in range(2, 1000):
    flg = True
    for p in prime_list:
        if i % p == 0:
            flg = False
            break
    if flg:
        prime_list.append(i)
cnt = 0
for i in range(N):
    l = list(map(int, input().split()))
    for j in l:
        if j in prime_list:
            cnt += 1
print(cnt)
