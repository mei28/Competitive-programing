from collections import Counter

l = list(map(int, input().split()))
cnter = Counter(l)

keys = list(cnter.keys())
if len(cnter.keys()) == 2:
    if cnter[keys[0]] == 2 or cnter[keys[0]] == 3:
        print("Yes")
        exit()

print("No")
