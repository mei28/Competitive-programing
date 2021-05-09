N = int(input())
A = list(map(int, input().split()))
dct = {}

for i in range(0, 200):
    dct[i] = 0

for a in A:
    tmp = a % 200
    dct[tmp] += 1

cnt = 0

for k, v in dct.items():
    if v == 0:
        continue
    cnt += v * (v - 1) // 2

print(cnt)
