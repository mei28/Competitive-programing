w = input()

dict_ = {}

for i in w:
    dict_.setdefault(i, 0)
    dict_[i] +=1

flg = True

for v in dict_.values():
    if v % 2 != 0:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")