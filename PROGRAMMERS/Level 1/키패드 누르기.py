def moveCount(start, end):
    if start == "*":
        start = 10
    elif start == "#":
        start = 12
    elif start == 0:
        start = 11

    if end == "*":
        end = 10
    elif end == "#":
        end = 12
    elif end == 0:
        end = 11

    count = 0
    # 같으면 종료
    while start != end:
        if start - end == 1 or start - end == -1:
            start = end
            return 1
        elif start == 2 or start == 5 or start == 8 or start == 11:
            if start < end:
                start += 3
                count += 1
            else:
                start -= 3
                count += 1
        elif start == 1:
            start += 1
            count += 1
        elif start == 3:
            start -= 1
            count += 1
        elif start == 4:
            start += 1
            count += 1
        elif start == 6:
            start -= 1
            count += 1
        elif start == 7:
            start += 1
            count += 1
        elif start == 9:
            start -= 1
            count += 1
        elif start == 10:
            start += 1
            count += 1
        elif start == 12:
            start -= 1
            count += 1
    return count


def solution(numbers, hand):
    answer = ""
    left = "*"
    right = "#"

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += "L"

        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += "R"

        else:
            leftCount = moveCount(left, i)
            rightCount = moveCount(right, i)
            if leftCount == rightCount:
                if hand == "left":
                    left = i
                    answer += "L"
                else:
                    right = i
                    answer += "R"
            elif leftCount < rightCount:
                left = i
                answer += "L"
            else:
                right = i
                answer += "R"

    return answer