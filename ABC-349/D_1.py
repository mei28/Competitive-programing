def optimal_good_sequences(L, R):
    intervals = []
    while L < R:
        power = 1
        while (L + power) <= R and ((L + power) & L) == L:
            power <<= 1

        if power > (R - L):
            power >>= 1

        intervals.append((L, L + power))
        L += power

    return intervals


L, R = map(int, input().split())
intervals = optimal_good_sequences(L, R)

print(len(intervals))
for l, r in intervals:
    print(l, r)
