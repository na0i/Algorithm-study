s = input()
symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0

for i in range(len(s)-1):
    current_num = symbol_dict[s[i]]
    next_num = symbol_dict[s[i+1]]

    if current_num < next_num:
        result -= current_num
    else:
        result += current_num

result += symbol_dict[s[-1]]
print(result)
