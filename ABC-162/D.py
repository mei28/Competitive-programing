n = int(input())
S = input()

r, g, b = 0, 0, 0

for s in S:
    if s == "R":
        r += 1
    if s == "G":
        g += 1
    if s == "B":
        b += 1

_all = r * g * b
sub = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if S[i] == S[j]:
            continue
        k = 2 * j - i

        if k >= n or S[k] == S[i] or S[k] == S[j]:
            continue

        sub += 1

print(_all - sub)
