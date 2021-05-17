if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)

    if len(A_set) == 1:
        if sum(A_set) == 0:
            print("Yes")
        else:
            print("No")
    elif len(A_set) == 2:
        a_1, _2 = sorted(A_set)
        if a_1 == 0:
            if A.count(a_1) * 3 == N:
                print("Yes")
            else:
                print("No")
        else:
            print("No")

    elif len(A_set) == 3:
        a_1, a_2, a_3 = A_set
        if A.count(a_3) == A.count(a_2) == A.count(a_1):
            if a_1 ^ a_2 == a_3:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
