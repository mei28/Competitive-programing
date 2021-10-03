n = input()
len_ = len(n)

ans = -1
for bits in range(1, 1 << len_ - 1):
    a = []
    b = []
    for j in range(len_):
        if (bits >> j) & 1:
            a.append(n[j])
        else:
            b.append(n[j])
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_ = "".join(a)
    b_ = "".join(b)
    ans = max(int(a_) * int(b_), ans)

print(ans)


# ans = -1
# for i in range(1, len_):
#     a = n[:i]
#     b = n[i:]
#     a = "".join(sorted(a, reverse=True))
#     b = "".join(sorted(b, reverse=True))
#     ans = max(int(a) * int(b), ans)
#     print(a, b, int(a) * int(b), ans)

# print(ans)
