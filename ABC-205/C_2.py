a, b, c = map(int, input().split())
import math

if a > 0 and b > 0:
    if math.log(a) - math.log(b) > 0:
        print(">")
    elif math.log(a) - math.log(b) < 0:
        print("<")
    else:
        print("=")

elif c % 2 == 0:
    if abs(a) > abs(b):
        print(">")
    elif abs(a) == abs(b):
        print("=")
    else:
        print("<")

else:
    if a > b:
        print(">")
    elif a == b:
        print("=")
    else:
        print("<")
