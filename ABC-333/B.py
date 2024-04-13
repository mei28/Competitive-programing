S = input()
T = input()
s1, s2 = S[0], S[1]
t1, t2 = T[0], T[1]

M = "ABCDE"

s_diff = abs(M.index(s1) - M.index(s2))
s_diff = min(5 - s_diff, s_diff)
t_diff = abs(M.index(t1) - M.index(t2))
t_diff = min(5 - t_diff, t_diff)

if s_diff == t_diff:
    print("Yes")
else:
    print("No")
