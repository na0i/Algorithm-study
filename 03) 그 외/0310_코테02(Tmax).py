queries = [["YOWRGB", "WOYRBG"], ["YOWRGB", "WOYRGB"], ["BGORWY", "BGORWY"]]
result = []


for i in range(len(queries)):
    # 위아래 바뀐게 같음
    if queries[i][0][0] == queries[i][1][2] and queries[i][0][2] == queries[i][1][0]:
        # 앞뒤 바뀐게 같음
        if queries[i][0][1] == queries[i][1][3] and queries[i][0][3] == queries[i][1][1]:
            # 왼오른 바뀐게 같음
            if queries[i][0][4] == queries[i][1][5] and queries[i][0][5] == queries[i][1][4]:
                result.append(0)
            # 왼오른 그냥 같음
            elif queries[i][0][4] == queries[i][1][4] and queries[i][0][5] == queries[i][1][5]:
                result.append(1)
            else:
                result.append(0)

    # 위아래 바뀐게 같음
    if queries[i][0][0] == queries[i][1][2] and queries[i][0][2] == queries[i][1][0]:
        # 왼오른 바뀐게 같음
        if queries[i][0][4] == queries[i][1][5] and queries[i][0][5] == queries[i][1][4]:
            # 앞뒤 바뀐게 같음
            if queries[i][0][1] == queries[i][1][3] and queries[i][0][3] == queries[i][1][1]:
                result.append(0)
            # 앞뒤 그냥 같음
            elif queries[i][0][1] == queries[i][1][1] and queries[i][0][3] == queries[i][1][3]:
                result.append(1)
            else:
                result.append(0)

    # 왼오른 바뀐게 같음
    if queries[i][0][4] == queries[i][1][5] and queries[i][0][5] == queries[i][1][4]:
        # 앞뒤 바뀐게 같음
        if queries[i][0][1] == queries[i][1][3] and queries[i][0][3] == queries[i][1][1]:
            # 위아래 바뀐게 같음
            if queries[i][0][0] == queries[i][1][2] and queries[i][0][2] == queries[i][1][0]:
                result.append(0)
            # 위아래 그냥 같음
            elif queries[i][0][0] == queries[i][1][0] and queries[i][0][2] == queries[i][1][2]:
                result.append(1)
            else:
                result.append(0)

    # 왼오른 바뀐게 같음
    if queries[i][0][4] == queries[i][1][5] and queries[i][0][5] == queries[i][1][4]:
        # 위아래 바뀐게 같음
        if queries[i][0][0] == queries[i][1][2] and queries[i][0][2] == queries[i][1][0]:
            # 앞뒤 바뀐게 같음
            if queries[i][0][0] == queries[i][1][2] and queries[i][0][2] == queries[i][1][0]:
                result.append(0)
            # 앞뒤 그냥 같음
            elif queries[i][0][0] == queries[i][1][0] and queries[i][0][2] == queries[i][1][2]:
                result.append(1)
            else:
                result.append(0)


    print(result)