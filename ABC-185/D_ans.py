n, m = map(int, input().split())
a = list(map(int, input().split())) + [0, n+1]
a.sort()

segment = []
for i in range(1, len(a)):
    segment.append(a[i] - a[i-1] - 1)

segment.sort(reverse=True)

while(len(segment) > 0 and segment[-1] == 0):
    segment.pop()

if len(segment) == 0:
    print(0)
    exit()

stamp_size = segment[-1]

ans = 0
for l in segment:
    ans += l // stamp_size
    if l % stamp_size != 0:
        ans += 1

print(ans)
