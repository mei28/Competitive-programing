N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

plus = []
_sum = 0
num = 0

for i in range(N):
    diff = A[i] - B[i]
    if diff < 0:
        _sum -= diff
        num += 1
    else:
        plus.append(diff)

if num == 0:
    print(0)
else:
    ans = num
    plus = sorted(plus, reverse=True)

    p = 0
    for i in range(len(plus)):
        p += plus[i]
        ans += 1
        if p >= _sum:
            break
    if p >= _sum:
        print(ans)
    else:
        print(-1)
