def solution(answers):

    one = 0
    two = 0
    three = 0
    answer = []

    for i in range(len(answers)):
        if i % 5 + 1 == answers[i]:
            one += 1

        if i % 2 == 0:
            if answers[i] == 2:
                two += 1
        else:
            if i % 8 == 1 and answers[i] == 1:
                two += 1
            elif i % 8 == 3 and answers[i] == 3:
                two += 1
            elif i % 8 == 5 and answers[i] == 4:
                two += 1
            elif i % 8 == 7 and answers[i] == 5:
                two += 1

        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                three += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                three += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                three += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                three += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                three += 1

    mx = max(one, two, three)
    if mx == one:
        answer.append(1)
    if mx == two:
        answer.append(2)
    if mx == three:
        answer.append(3)

    return answer