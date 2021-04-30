N = int(input())
S = [input() for _ in range(N)]

set_ = set()

for i, s in enumerate(S):
    if s in set_:
        continue
    else:
        set_.add(s)
        print(i + 1)
