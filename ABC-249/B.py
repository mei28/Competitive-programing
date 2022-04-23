import re

S = input()
n = len(S)


def check_upper_char(string):
    result = re.search("[A-Z]", string)
    return True if result else False


def check_lower_char(string):
    result = re.search("[a-z]", string)
    return True if result else False


if check_upper_char(S) and check_lower_char(S) and len(set(list(S))) == n:
    print("Yes")
    exit()

print("No")
