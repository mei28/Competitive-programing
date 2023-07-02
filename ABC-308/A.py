S = list(map(int, input().split()))
T = sorted(S)
for s, t in zip(S, T):
    if s != t:
        print("No")
        exit()

for a in S:
    if a < 100 or 675 < a:
        print("No")
        exit()
    if a % 25 != 0:
        print("No")
        exit()
print("Yes")
