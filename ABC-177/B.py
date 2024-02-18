S = input()
T = input()

min_cnt = 9999999999
for i in range(0, len(S) - len(T) + 1):
    s = S[i : i + len(T)]
    cnt = 0
    for m, n in zip(s, T):
        if m != n:
            cnt += 1
    min_cnt = min(min_cnt, cnt)

print(min_cnt)
