S = input()
T = input()
from itertools import groupby


# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


S_ = runLengthEncode(S)
T_ = runLengthEncode(T)


if len(S_) != len(T_):
    print("No")
    exit()

for s, t in zip(S_, T_):
    c, a = s
    d, b = t

    if c != d:
        print("No")
        exit()

    if a != b:
        if a > b or a==1:
            print("No")
            exit()

print("Yes")
