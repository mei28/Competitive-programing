from typing import List

n = int(input())
s = input()

li: List[str] = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            li.append(str(i) + str(j) + str(k))

result = 0


for l in li:
    idx = 0
    for c in s:
        if l[idx] == c:
            idx += 1
        if idx >= 3:
            result += 1
            break
print(result)
