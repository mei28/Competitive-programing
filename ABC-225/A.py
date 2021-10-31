s = input()

se = set()
for i in s:
    se.add(i)

if len(se) == 3:
    print(6)
elif len(se) == 2:
    print(3)
else:
    print(1)
