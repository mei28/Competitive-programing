N = int(input())

N = N + 1

N_str = str(N)

first_N = int(N_str[0]) - 1
num = len(N_str)-1

print(num*9+first_N)