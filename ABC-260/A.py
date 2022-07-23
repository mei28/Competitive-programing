from collections import Counter

S = input()
cnt = Counter(S)
for k, v in cnt.items():
    if v == 1:
        print(k)
        exit()
print(-1)
