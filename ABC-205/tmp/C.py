def main():
    def solve():
        if C % 2 == 1:
            if A < B:
                return "<"
            elif A > B:
                return ">"
            else:
                return "="
        else:
            if abs(A) < abs(B):
                return "<"
            elif abs(A) > abs(B):
                return ">"
            else:
                return "="

    A, B, C = map(int, input().split())
    print(solve())


if __name__ == "__main__":
    main()
