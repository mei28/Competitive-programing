T = int(input())


def solve(n: int):
    if n % 4 == 0:
        print("Even")
    elif n % 2 == 0:
        print("Same")
    else:
        print("Odd")


for _ in range(T):
    n = int(input())
    solve(n)
