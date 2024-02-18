k = int(input())


def conver(x):
    ans: str = ""
    while x > 0:
        ans += str(x % 2)
        x //= 2

    return ans[::-1]


def output(x: str):
    ans = ""
    for i in x:
        if i == "1":
            ans += "2"
        else:
            ans += "0"
    print(ans)


# output(conver(k))
print(conver(k).replace("1", "2"))
