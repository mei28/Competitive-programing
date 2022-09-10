s = input()
t = input()

n = len(s)
if t[:n] == s:
    print("Yes")
else:
    print("No")
