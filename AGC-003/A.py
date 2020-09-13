S = input()
set_ = set()

for i in S:
    set_.add(i)

if len(set_) == 4:
    print("Yes")
elif len(set_) == 2:
    if 'N' in set_ and 'S' in set_:
        print("Yes")
    elif 'E' in set_ and 'W' in set_:
        print("Yes")
    else:
        print("No")
else:
    print("No")