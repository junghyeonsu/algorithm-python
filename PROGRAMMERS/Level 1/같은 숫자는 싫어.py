def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        last = len(answer) - 1
        if i == answer[last]:
            continue
        else:
            answer.append(i)
    return answer