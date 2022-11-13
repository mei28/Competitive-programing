n = int(input())

group = set()
group.add(1)
for _ in range(n):
    a, b = map(int, input().split())
    if a in group or b in group:
        group.add(a)
        group.add(b)
print(max(group))
