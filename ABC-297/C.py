h, w = map(int, input().split())
S = [input() for _ in range(h)]
T = []

for s in S:
    T.append(s.replace("TT", "PC"))

for t in T:
    print("".join(t))
