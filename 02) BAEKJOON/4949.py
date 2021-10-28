while True:
    sentence = input()

    if sentence == '.':
        break

    stack = []
    for s in range(len(sentence)):
        if sentence[s] != '(' and sentence[s] != ')' and sentence[s] != '[' and sentence[s] != ']':
            continue
        else:
            if stack:
                if sentence[s] == ')' and stack[-1] == '(':
                    stack.pop()
                elif sentence[s] == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(sentence[s])
            else:
                stack.append(sentence[s])

    if stack:
        print('no')
    else:
        print('yes')