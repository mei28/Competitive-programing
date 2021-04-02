Sa = input()
Sb = input()
Sc = input()

flg = "a"

while len(Sa) >= 0 and len(Sb) >= 0 and len(Sc) >= 0:
    if flg == "a":
        if len(Sa) == 0:
            print("A")
            exit()
        flg = Sa[0]
        Sa = Sa[1:]
    elif flg == "b":
        if len(Sb) == 0:
            print("B")
            exit()
        flg = Sb[0]
        Sb = Sb[1:]
    elif flg == "c":
        if len(Sc) == 0:
            print("C")
            exit()
        flg = Sc[0]
        Sc = Sc[1:]
    else:
        break
