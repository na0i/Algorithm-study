mapping_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
result = []
digits = '23'


def recursive(check, temp_str):
    if check == len(digits):
        result.append(temp_str)
        return

    for i in mapping_dict[digits[check]]:
        recursive(check + 1, temp_str + i)


recursive(0, '')

print(result)