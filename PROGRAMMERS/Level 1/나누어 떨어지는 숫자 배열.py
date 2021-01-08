def solution(arr, divisor):
    answer = [-1]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 1: 
        return answer
    else:
        answer.sort()
        return answer[1:]