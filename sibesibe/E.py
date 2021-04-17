S = input()
N = len(S) - 1

ans = 0

for bit in range(1 << N):
    f = S[0]
    for j in range(N):
        if bit >> j & 1:
            f += "+"
        f += S[j + 1]

    ans += sum(map(int, f.split("+")))

print(ans)
