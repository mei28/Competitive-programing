from bisect import bisect_right, bisect_left

t = int(input())
ns = [int(input()) for _ in range(t)]

cands = []
for i in range(65):
    for j in range(i + 1, 65):
        for k in range(j + 1, 65):
            tmp = ["0"] * 65
            tmp[i] = "1"
            tmp[j] = "1"
            tmp[k] = "1"
            if i != j != k:
                tmp = "".join(tmp)
                cands.append(int(tmp, 2))
cands.sort()
for n in ns:
    if n < 7:
        print(-1)
        continue
    idx = bisect_right(cands, n)
    print(cands[idx - 1])
