n = int(input())
A = list(map(int, input().split()))
_all = sum(A)
_part = _all * 0.1
B = A + A

S = [0] * (2 * n + 1)
for i in range(2 * n):
    S[i + 1] = S[i] + B[i]
j = 0
now = 0
for i in range(n):
    while now < _part:
        now += B[j]

        j += 1

    if now == _part:
        print("Yes")
        exit()
    now -= B[i]
print("No")
