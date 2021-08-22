s, k = input().split()
k = int(k)

a = [i for i in s]
import itertools

l = set()
for v in itertools.permutations(a, len(s)):
    b = "".join(v)
    l.add(b)

l = list(l)
l = sorted(l)
print(l[k - 1])
