S = input()

S = S.replace("eraser", "")
S = S.replace("erase", "")
S = S.replace("dreamer", "")
S = S.replace("dream", "")

print("YES") if S == "" else print("NO")
