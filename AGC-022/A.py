s = list(input())
letters = list("abcdefghijklmnopqrstuvwxyz")
if len(s) != 26:
    for i in letters:
        if not (i in s):
            s.append(i)
            break
    print("".join(s))
else:
    check = False
    for i in range(25, 0, -1):
        if s[i] > s[i - 1]:
            check = True
            break
    if check:
        temp = s[: i - 1]
        plus = ["z"]
        for j in s[i:]:
            if s[i - 1] < j < plus[0]:
                plus = [j]
        print("".join(temp + plus))

    else:
        print(-1)
