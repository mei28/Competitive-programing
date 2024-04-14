def find_next_good_sequence(start, end):
    power = 0
    while (1 << (power + 1)) <= start:
        power += 1
    original_power = power
    while power >= 0:
        j = start >> power
        l = j << power
        r = (j + 1) << power
        if l == start and r <= end:
            return r
        power -= 1

    power = original_power + 1
    while True:
        j = start >> power
        l = j << power
        r = (j + 1) << power
        if l >= start and r <= end:
            return r
        if (1 << (power + 1)) > end:
            break
        power += 1

    return start + 1


def optimal_good_sequences(L, R):
    intervals = []
    current = L
    while current < R:
        next_bound = find_next_good_sequence(current, R)
        intervals.append((current, next_bound))
        current = next_bound
    return intervals


L, R = map(int, input().split())

intervals = optimal_good_sequences(L, R)
M = len(intervals)

print(M)
for l, r in intervals:
    print(l, r)
