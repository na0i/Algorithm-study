palindrome = "aa"
half_palindrome = palindrome[:len(palindrome) // 2]
result = ''
if len(palindrome) > 1:
    half_palindrome = palindrome[:len(palindrome) // 2]

    only_a = True

    for i in range(len(half_palindrome)):
        if half_palindrome[i] != 'a':
            half_palindrome = half_palindrome[:i] + 'a' + half_palindrome[i + 1:]
            result = half_palindrome + palindrome[len(palindrome) // 2:]
            only_a = False

    if only_a and len(palindrome) > 2:
        half_palindrome = half_palindrome[:-2] + 'b'
        result = palindrome[:len(palindrome) // 2 + 1] + half_palindrome

    elif only_a and len(palindrome) <= 2:
        result = 'ab'

else:
    result = ""

print(result)