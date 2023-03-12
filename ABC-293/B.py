n = int(input())
A = [-1] + list(map(int, input().split()))
flg = [False] * (n + 1)


for i, a in enumerate(A):
    if i == 0:
        continue
    if not flg[i]:
        flg[a] = True

print(len(flg) - sum(flg) - 1)

for i in range(len(flg)):
    if i == 0:
        continue
    if flg[i]:
        continue
    print(i, end=" ")
