emails = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
cnt = 0
for email in emails:
    flag = True
    email_split_1 = list(map(str, email.split('@')))

    # print(email_split_1)
    # ['d', 'co', 'm.com']
    # ['a', 'abc.com']
    # ['b', 'def.com']
    # ['c', 'ghi.net']

    if len(email_split_1) != 2:
        flag = False

    else:
        name = email_split_1[0]
        if len(name) < 1:
            flag = False
        else:
            for i in range(len(name)):
                if 97 <= ord(name[i]) <= 122 or ord(name[i]) == 46:
                    continue
                else:
                    flag = False

            email_split_2 = list(map(str, email_split_1[1].split('.')))
            # ['a', 'bc', 'com']
            # ['def', 'com']
            # ['ghi', 'net']

            if len(email_split_2) != 2:
                flag = False

            else:
                domain_name = email_split_2[0]

                for d in range(len(domain_name)):
                    if 97 <= ord(domain_name[d]) <= 122:
                        continue
                    else:
                        flag = False

                toplevel = email_split_2[1]
                if toplevel != 'com' and toplevel != 'net' and toplevel != 'org':
                    flag = False

    if flag == True:
        cnt += 1

print(cnt)