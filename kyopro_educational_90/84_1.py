from typing import List

n = int(input())
s = input()

cnt = 0
vec: List[List[int]] = []
for i in range(len(s)):
    cnt += 1
    if i == len(s) - 1 or s[i] != s[i + 1]:
        vec.append([i, cnt])
        cnt = 0

ret = 0

for i in vec:
    ret += i[1] * (i[1] + 1) // 2

print(n * (n + 1) // 2 - ret)
