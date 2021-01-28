def solution(dartResult):
    items = list(dartResult)
    real = []
    for i in range(len(items)):
        if items[i] == "1" and items[i + 1] == "0":
            continue
        elif items[i] == "0" and items[i - 1] == "1":
            real.append("10")
        else:
            real.append(items[i])

    answer = []
    for i in range(1, len(real)):
        if real[i] == "S":
            answer.append(int(real[i - 1]) ** 1)
        elif real[i] == "D":
            answer.append(int(real[i - 1]) ** 2)
        elif real[i] == "T":
            answer.append(int(real[i - 1]) ** 3)

        if real[i] == "*":
            if len(answer) >= 2:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
        elif real[i] == "#":
            answer[-1] *= -1

    return sum(answer)