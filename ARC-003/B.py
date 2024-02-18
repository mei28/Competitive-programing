n = int(input())

l = []

for i in range(n):
    s = input()
    rev_s = s[::-1]
    l.append((s, rev_s))


l = list(sorted(l, key=lambda x: x[1]))

for i in l:
    print(i[0])
