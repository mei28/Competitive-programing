N = 1


def encode(s: str) -> str:
    ret = ""
    a = "abcdefghijklm"
    b = "nopqrstuvwxyz"
    for i in s:
        if i in a:
            tmp = chr(ord(i) + 13)
        else:
            tmp = chr(ord(i) - 13)
        ret += tmp
    return ret


for i in range(N):
    print(encode(input()))
