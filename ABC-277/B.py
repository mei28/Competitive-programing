n = int(input())
S = [input() for _ in range(n)]
set_ = set()

A = ["H", "D", "C", "S"]
B = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
for s in S:
    t = s[0]
    u = s[1]
    if t not in A:
        print("No")
        exit()
    if u not in B:
        print("No")
        exit()

    set_.add(s)

if len(set_) == n:
    print("Yes")
else:
    print("No")
