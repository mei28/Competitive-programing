S = input()
len_S = len(S)
dif = len_S - 7

for i in range(8):
    temp = S[0:i] + S[dif+i:]
    if temp == "keyence":
        print("YES")
        exit()
print("NO")
