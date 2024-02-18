print("Weak") if len(set(X := input())) == 1 else print("Weak") if all(
    (int(X[i]) + 1) % 10 == int(X[i + 1]) for i in range(3)
) else print("Strong")
