s = input()

t = [0] * (10 ** 6 + 10)
l = 3 + 5 * 10 ** 5
r = l

flip = False


def push_front(c):
    global l, t
    l -= 1
    t[l] = c


def push_back(c):
    global r, t
    t[r] = c
    r += 1


def squash_front():
    global l
    if r - l >= 2 and t[l] == t[l + 1]:
        l += 2


def squash_back():
    global r
    if r - l >= 2 and t[r - 1] == t[r - 2]:
        r -= 2


for c in s:
    if c == "R":
        flip ^= 1
    else:
        if flip:
            push_front(c)
            squash_front()
        else:
            push_back(c)
            squash_back()

ans = "".join(t[l:r])
if flip:
    ans = ans[::-1]

print(ans)

###################################################
# S = input()

# rev = False

# t = [0] * (10 ** 6 + 10)
# # l-rの間を考える
# l = 5 * 10 ** 5 + 3
# r = l


# def push_front(c):
#     global l, t
#     l -= 1
#     t[l] = c


# def push_back(c):
#     global r, t
#     t[r] = c
#     r += 1


# def squash_front():
#     global l, t
#     if r - l >= 2 and t[l] == t[l + 1]:
#         l += 2


# def squash_end():
#     global l, t
#     if r - l >= 2 and t[r - 2] == t[r - 1]:
#         l -= 2


# for c in S:
#     if c == "R":
#         rev = not rev
#     else:
#         if rev:
#             push_front(c)
#             squash_front()
#         else:
#             push_back(c)
#             squash_end()

# ans = "".join(t[l:r])
# if rev:
#     print(ans[::-1])
# else:
#     print(ans)
