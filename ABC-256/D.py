n = int(input())
ma = 2 * 10 ** 5 + 10
imo = [0] * ma

for _ in range(n):
    l, r = map(int, input().split())
    imo[l] += 1
    imo[r] -= 1

for i in range(ma):
    if 0 < i:
        imo[i] += imo[i - 1]

ans = []
flg = False
for i in range(ma):
    if flg == False and imo[i] > 0:
        flg = True
        start = i
    elif flg == True and imo[i] == 0:
        flg = False
        end = i
        ans.append((start, end))

for a in ans:
    print(*a)
