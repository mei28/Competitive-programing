def is_1122_string(s):
    n = len(s)
    if n % 2 == 0:
        return False
    mid = n // 2
    return s[:mid] == "1" * mid and s[mid] == '/' and s[mid+1:] == "2" * mid

n = int(input())
s = input()

if is_1122_string(s):
    print("Yes")
else:
    print("No")
