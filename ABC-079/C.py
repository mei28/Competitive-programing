line = input()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

op = ['+', '-']

if a + b + c + d == 7:
    print(f'{a}+{b}+{c}+{d}=7')

elif a + b + c - d == 7:
    print(f'{a}+{b}+{c}-{d}=7')

elif a + b - c + d == 7:
    print(f'{a}+{b}-{c}+{d}=7')

elif a + b - c - d == 7:
    print(f'{a}+{b}-{c}-{d}=7')

elif a - b + c + d == 7:
    print(f'{a}-{b}+{c}+{d}=7')

elif a - b + c - d == 7:
    print(f'{a}-{b}+{c}-{d}=7')

elif a - b - c + d == 7:
    print(f'{a}-{b}-{c}+{d}=7')

elif a - b + c - d == 7:
    print(f'{a}-{b}-{c}-{d}=7')
