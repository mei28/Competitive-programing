s = input()
k = int(input())

set_ = set()
for i in range(0, len(s) - k + 1):
    a = s[i : i + k]
    set_.add(a)

print(len(set_))
