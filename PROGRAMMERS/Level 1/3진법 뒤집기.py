def solution(n):
    answer = ""
    while n >= 1:
        answer += str(n % 3)
        n = n // 3
    leng = len(answer) - 1
    result = 0
    for i in answer:
        result += int(i) * (3 ** leng)
        leng -= 1

    return result