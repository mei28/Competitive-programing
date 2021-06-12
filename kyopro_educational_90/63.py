from collections import Counter


def same(col: int, bit: int) -> int:
    res = -1
    for i, a in enumerate(col):
        if (bit >> i) & 1:
            if res != -1 and res != a:
                return -1
            res = a
    return res


popcnt = lambda x: bin(x).count("1")
h, w = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]

ans = 0

for bit in range(1, 1 << h):
    cnt = Counter()
    for col in zip(*p):
        a = same(col, bit)
        if a != -1:
            cnt[a] += 1
    if cnt:
        now = max(cnt.values()) * popcnt(bit)
        if now > ans:
            ans = now

print(ans)
