from collections import Counter

s = input()

cnt = Counter(s)

dct = {i: 0 for i in range(len(s) + 1)}


for k, v in cnt.items():
    dct[v] += 1


for k, v in dct.items():
    if v == 0 or v == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")
