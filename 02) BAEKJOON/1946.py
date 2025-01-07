T = int(input())
for tc in range(T):
    applicants = int(input())
    scores = []
    for i in range(applicants):
        D, I = map(int, input().split())
        scores.append([D, I])

    sorted_scores = sorted(scores, key=lambda x:x[0])

    criteria = sorted_scores[0][1]
    passed = [sorted_scores[0]]

    for i in range(1, len(sorted_scores)):
        if sorted_scores[i][1] < criteria:
            criteria = sorted_scores[i][1]
            passed.append(sorted_scores[i])

    print(len(passed))
