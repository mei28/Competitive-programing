S = input()
alp_set = set()
for s in S:
    alp_set.add(s)

if len(alp_set) == len(S):
    print("yes")
else:
    print("no")
