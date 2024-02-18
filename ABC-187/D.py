N = int(input())

C = []

for _ in range(N):
    C.append(list(map(int, input().split())))

Aotaka = sum(map(lambda x: x[0], C))

dec = list(map(lambda x: -2 * x[0] - x[1], C))
dec.sort()

cnt = 0
while Aotaka >= 0:
    Aotaka += dec[cnt]
    cnt += 1

print(cnt)
