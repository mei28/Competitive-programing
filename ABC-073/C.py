N = int(input())
freq = {}
res = 0
for i in range(N):
    A = int(input())
    if A in freq:
        freq[A] += 1
    else:
        freq[A] = 1
    if freq[A] % 2 == 0:
        res -= 1
    else:
        res += 1
print(res)
