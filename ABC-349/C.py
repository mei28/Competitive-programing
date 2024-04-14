def is_airport_code(S, T):
    it = iter(S)
    T_index = 0

    for char in it:
        if T[T_index] == char.upper():
            T_index += 1
            if T_index == len(T):
                return True
        if T_index == 2 and T[-1] == "X":
            return True

    return False


s = input()
t = input()
result = is_airport_code(s, t)
if result:
    print("Yes")
else:
    print("No")
