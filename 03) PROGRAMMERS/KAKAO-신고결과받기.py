id_list = ["muzi", "frodo", "apeach", "neo"]
id_list2 = ["con", "ryan"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

report = list(set(report))
cnt = [0] * len(id_list)
result = []
for i in range(len(report)):
    reportSplit = report[i].split(' ')
    a = reportSplit[0]
    b = reportSplit[1]

    result.append(b)

    print(a, b)