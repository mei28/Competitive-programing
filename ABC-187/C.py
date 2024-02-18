N = int(input())

key_bi = set()
key_ = set()
for i in range(N):
    a = input()

    if a[0] == "!":
        tmp = a[1:]
        key_bi.add(tmp)
    else:
        tmp = a
        key_.add(tmp)


if len(key_bi & key_) > 0:
    print(list(key_bi & key_)[0])
else:
    print("satisfiable")
