from collections import Counter

def solve(s):
    if len(s) % 2 != 0:
        return False
    if any(s[i] != s[i+1] for i in range(0, len(s), 2)):
        return False
    counts = Counter(s)
    return all(count == 2 for count in counts.values())

s = input()

if solve(s):
    print("Yes")
else:
    print("No")
