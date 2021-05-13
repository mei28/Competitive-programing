def rls(s: str) -> list:
    tmp, count, ans = s[0], 1, []

    for i in range(1, len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append(count)
            tmp = s[i]
            count = 1
    ans.append(count)
    return ans


if __name__ == "__main__":
    pass
    S = input()
    l = rls(S)

    print(len(l) - 1)
