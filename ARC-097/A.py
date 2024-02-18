s = input()
k = int(input())
n = len(s)

se = set()

for i in range(n):
    for j in range(1, 6):
        if i + j > n:
            continue
        se.add(s[i : i + j])

li = list(se)
li.sort()
print(li[k - 1])
