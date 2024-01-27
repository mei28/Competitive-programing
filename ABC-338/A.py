s = input()

if len(s) == 1:
    if s.isupper():
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if s[0].isupper() and s[1:].islower():
    print("Yes")
else:
    print("No")
