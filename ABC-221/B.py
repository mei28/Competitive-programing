s = input()
t = input()

if s == t:
    print("Yes")
else:
    _s = [i for i in s]
    for i in range(0, len(s) - 1):
        __s = _s.copy()
        __s[i], __s[i + 1] = __s[i + 1], __s[i]
        if "".join(__s) == t:
            print("Yes")
            exit()

    print("No")
