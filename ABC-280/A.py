h, w = map(int, input().split())
S = [input() for _ in range(h)]
print(sum([s.count("#") for s in S]))
