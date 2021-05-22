S = input()
ans = ""
for i in S[::-1]:
    if i == "0":
        ans += "0"
    elif i == "1":
        ans += "1"
    elif i == "6":
        ans += "9"
    elif i == "8":
        ans += "8"
    elif i == "9":
        ans += "6"


print(ans)
