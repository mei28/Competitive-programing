n = int(input())
S = [input() for _ in range(n)]
set_ = set()
dct = {}

for s in S:
    if s not in set_:
        dct[s] = 1
        set_.add(s)
        print(s)
    else:
        print(f"{s}({dct[s]})")
        dct[s] += 1
