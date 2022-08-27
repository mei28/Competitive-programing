from collections import Counter
import string

alp = string.ascii_uppercase

n, m = map(int, input().split())
name = input()
kit = input()

name_cnt = Counter(name)
kit_cnt = Counter(kit)

ans = -1

for a in alp:
    if a in name_cnt.keys():
        if a not in kit_cnt.keys():
            print(-1)
            exit()
        i = name_cnt[a]
        j = kit_cnt[a]
        ans = max(ans, (i + j - 1) // j)

print(ans)
