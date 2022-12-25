S = input()
n = len(S)

V = [set() for _ in range(n)]
used = set()

now = 0
for s in S:
    if s == "(":
        now += 1
    elif s == ")":
        for c in V[now]:
            used.remove(c)
        now -= 1
    else:
        if s in used:
            print("No")
            exit()
        used.add(s)
        V[now].add(s)
print("Yes")
