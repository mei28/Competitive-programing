s1 = input()
s2 = input()

if s1[0] == "." and s1[1] == "#" and s2[0] == "#" and s2[1] == ".":
    print("No")
    exit()
if s1[1] == "." and s1[0] == "#" and s2[1] == "#" and s2[0] == ".":
    print("No")
    exit()
else:
    print("Yes")
