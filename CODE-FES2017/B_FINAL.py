s = input()
a = s.count("a")
b = s.count("b")
c = s.count("c")

result = max(a, b, c) <= min(a, b, c) + 1
print(["NO", "YES"][result])
