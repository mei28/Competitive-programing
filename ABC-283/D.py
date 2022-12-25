import string
from collections import deque

S = input()

if S.count("(") != S.count(")"):
    print("No")
    exit()

se = set()
q = deque()
for s in S:
    if s in string.ascii_lowercase:
        if s not in se:
            se.add(s)
        else:
            print("No")
            exit()
    if s == ")":
        pass

print("Yes")
