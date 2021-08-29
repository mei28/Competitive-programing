n = int(input())

tmp = 1
i = 0
for i in range(130):
    if tmp > n:
        break
    tmp *= 2


for bits in range(1 << 120):
    tmp = 0
    ans = []
    for j in range(120):
        if (bits >> j) & 1:
            tmp += 1
            ans.append("A")
        else:
            tmp *= 2
            ans.append("B")

        if tmp == n:
            print("".join(ans))
            exit()
        if tmp > n:
            continue
