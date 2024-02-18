x = input()
A = list(map(int, x))
S = [0] * (len(x) + 1)
for i in range(len(x)):
    S[i + 1] = S[i] + A[i]

S = S[::-1]
res = []
rem = 0

for x in S:
    rem += x
    res.append(rem % 10)
    rem //= 10
while rem > 0:
    res.append(rem % 10)
    rem //= 10

ans = res[::-1]
print(*ans, sep="")
