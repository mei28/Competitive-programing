def find_palindromic_number(n):
    if n == 1:
        return 0

    def count_palindromes_by_length(length):
        if length == 1:
            return 10  
        half_length = (length + 1) // 2
        return 9 * 10 ** (half_length - 1)

    length = 1
    count = 0

    while count < n:
        num_palindromes = count_palindromes_by_length(length)
        if count + num_palindromes >= n:
            break
        count += num_palindromes
        length += 1

    position_in_length = n - count - 1
    half_length = (length + 1) // 2
    if length == 1:
        return position_in_length

    start = 10 ** (half_length - 1)
    number = start + position_in_length
    first_half = str(number)

    if length % 2 == 0:
        palindrome = first_half + first_half[::-1]
    else:
        palindrome = first_half + first_half[-2::-1]

    return int(palindrome)

n = int(input())
print(find_palindromic_number(n))

