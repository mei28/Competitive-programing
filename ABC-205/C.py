a, b, c = map(int, input().split())

if a >= 1:
    if b >= 1:
        if a > b:
            print(">")
        elif a == b:
            print("=")
        else:
            print("<")
    elif -1 < b < 1:
        print(">")
    else:
        if c%2==0:

    pass
elif -1 < a < 1:
    pass
else:
    pass

# if a > 0 and b > 0:
#     if a > 1 and b > 1:
#         if a > b:
#             print(">")
#         elif a == b:
#             print("=")
#         else:
#             print("<")

#     elif a > 1 and b <= 1:
#         print(">")
#     elif a <= 1 and b > 1:
#         print("<")
#     elif a == 1 and b == 1:
#         print("=")
#     else:
#         if a < c:
#             print(">")
#         else:
#             print("<")
