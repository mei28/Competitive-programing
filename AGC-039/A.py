def rls(s):
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
    S = input()
    K = int(input())
    r = rls(S)
    ans = 0
    if S[0] != S[-1]:
        for i in r:
            ans += i // 2
        ans *= K
    else:
        if len(r) == 1:
            ans = int(r[0]) * K // 2
        else:
            left = int(r[0])
            right = int(r[-1])
            mid = 0
            for i in range(1, len(r) - 1):
                mid += int(r[i]) // 2
            ans = mid * K + (left + right) // 2 * (K - 1) + left // 2 + right // 2
    print(ans)
