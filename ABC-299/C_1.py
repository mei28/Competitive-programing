n = int(input())
SS = input().split("-")

ans = -1
for s in SS:
    ans = max(len(s), ans)
print(-1 if ans <= 0 else ans)
